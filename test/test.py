import xlrd
import numpy as np
from sklearn import metrics

def loadFile(fileName):
    data = xlrd.open_workbook(fileName)
    table = data.sheets()[0]
    first = table.col_values(0)
    second = table.col_values(1)
    tri = table.col_values(2)
    nrows = table.nrows
    dataSet = []
    classData = []
    for i in range(nrows):
        dataSet.append([float(first[i]), float(second[i])])
        classData.append(int(tri[i]))
    return (dataSet,classData)


if __name__ == "__main__":
    sourceFile = "/home/hhd/workspace/homework/machineleanning/gaussianClassification/data/data.xlsx"
    resultFile = "/home/hhd/workspace/homework/machineleanning/gaussianClassification/data/output.xlsx"

    classMap = {}
    sourceData,sourceClass = loadFile(sourceFile)
    resultData,resultClass = loadFile(resultFile)
    
    score = metrics.adjusted_mutual_info_score(sourceClass,resultClass) 

    print "get score >>> ",score