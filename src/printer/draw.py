#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def showCluster(data, k, clusterAssment, fileName):
    dataMat = np.mat(data)
    numSamples, dim = dataMat.shape
    if dim != 2:
        print("Sorry! I can not draw because the dimension of your data is not 2!")
        return 1

    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("Sorry! Your k is too large!")
        return 1

        # draw all samples
    for i in range(numSamples):
        markIndex = int(clusterAssment[i])
        plt.plot(dataMat[i, 0], dataMat[i, 1], mark[markIndex - 1])
    plt.savefig(fileName)
    # plt.show()
