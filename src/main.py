#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
from tools.tools import *
from machinLearning.GaussianMuti import *
from printer.draw import *


if __name__ == "__main__":

    k = 3
    inputFile = '/home/hhd/workspace/homework/machineleanning/gaussianClassification/data/data.xlsx'
    outputFile = '/home/hhd/workspace/homework/machineleanning/gaussianClassification/data/'
    maxLoop = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hk:i:o:l:", [
                                   "inputFile=", "outputFile="])
    except getopt.GetoptError:
        showHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            showHelp()
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            inputFile = arg
        elif opt in ("-o", "--outputFile"):
            outputFile = arg
        elif opt == '-k':
            k = int(arg)
        elif opt == '-l':
            maxLoop = int(arg)
    if(k < 1):
        print "k必须大于1"
    # if(outputFile == ""):
    #     print "必须指定输出文件"
    if(maxLoop < 0):
        print "迭代次数必须大于0"

    dataSet,result = loadFile(inputFile)
    classMat = gaussian(dataSet, k, maxLoop)
    writeFile(dataSet, classMat, outputFile+"output.xlsx")
    showCluster(dataSet, k, classMat, outputFile+'output.png')
    showCluster(dataSet, 3, result, outputFile+'input.png')

