#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import math


def prob(x, mu, sigma):
    n = np.shape(x)[1]
    expOn = float(-0.5 * (x - mu) * (sigma.I) * ((x - mu).T))
    divBy = pow(2 * np.pi, n / 2) * pow(np.linalg.det(sigma),
                                        0.5)  # np.linalg.det 计算矩阵的行列式
    return pow(np.e, expOn) / divBy


def gaussian(data, k, maxLoop=0):
    sourceMat = np.mat(data)
    r, c = sourceMat.shape  # r个c维的数据
    gamma = np.mat(np.zeros((r, k)))  # 初始化隶属度矩阵为零
    # classMat = np.zeros((1, r))  # 初始化分类结果
    classMat = [0]*r
    changeFlage = True  # 标记分类结果是否有变化
    count = 0  # 记录循环次数
    alpha = []                  # 混合参数
    mu = []                     # 概率分布期望参数
    sigma = [np.mat([[0.1, 0], [0, 0.1]]) for x in range(k)]  # 初始化概率分布协方差矩阵

    cutIndex = int(math.floor((r-1) / k))  # 期望参数取值分片
    for i in range(k):
        index = (i + 1) * cutIndex  # 期望取值下标
        alpha.append(1.0 / k)  # 初始化混合参数
        mu.append(sourceMat[index, :])  # 初始化期望参数

    while changeFlage:
        changeFlage = False
        if maxLoop > 0 and count == maxLoop:
            print "loop limit >>>", count
            break
        else:
            for i in range(r):
                sumAlphaMulP = 0
                for j in range(k):
                    # 4.计算混合成分生成的后验概率，即gamma
                    gamma[i, j] = alpha[j] * \
                        prob(sourceMat[i, :], mu[j], sigma[j])
                    sumAlphaMulP += gamma[i, j]
                for j in range(k):
                    gamma[i, j] /= sumAlphaMulP
            sumGama = np.sum(gamma, axis=0)

            for j in range(k):
                mu[j] = np.mat(np.zeros((1, c)))
                sigma[j] = np.mat(np.zeros((c, c)))
                for i in range(r):
                    mu[j] += gamma[i, j] * sourceMat[i, :]
                mu[j] /= sumGama[0, j]

                for i in range(r):
                    sigma[j] += gamma[i, j] * \
                        (sourceMat[i, :] - mu[j]).T * (sourceMat[i, :] - mu[j])
                sigma[j] /= sumGama[0, j]
                alpha[j] = sumGama[0, j] / r

            count += 1
            for i in range(r):
                index = np.argmax(gamma[i, :]) + 1
                if index != classMat[i]:
                    classMat[i] = int(index)  # 获取分类结果
                    changeFlage = True  # 分类结果被修改
    print "loop count >>>",count
    print "alpha >>>",alpha
    print "sigma >>>",sigma
    print "mu >>>",mu
    return classMat
