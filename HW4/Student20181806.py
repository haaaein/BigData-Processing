#!/usr/bin/pyton3

import sys
import numpy as np
import operator
from os import listdir

train = sys.argv[1]
test = sys.argv[2]
testDigits = listdir(test)
trainDigits = listdir(train)

def fileToVector(filename): 
    vector = np.zeros((1, 1024)) 

    with open(filename) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])

        return vector   

def createDataSet(dataset):
    m = len(trainDigits)
    group = np.zeros((m, 1024)) #32 X 32
    labels = []
    
    for i in range(m): 
        file_name = trainDigits[i]
        answer = int(file_name.split('_')[0]) 
        labels.append(answer)
        group[i, :] = fileToVector(dataset + '/' + file_name)

    return group, labels 

def classify0(inX, dataSet, labels, k): 
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2 
    sqDistances = sqDiffMat.sum(axis = 1) 
    distances = sqDistances ** 0.5 
    sortedDistIndicies = distances.argsort() 
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]] 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True) 
    return sortedClassCount[0][0]     

group, labels = createDataSet(train)

for k in range(1, 21):
    count = 0 
    error = 0 
    
    for i in range(len(testDigits)): 
        testData = fileToVector(test + '/' + testDigits[i])
        answer = int(testDigits[i].split('_')[0])
        expect = classify0(testData, group, labels, k)
        if answer != expect :
            error += 1
        count += 1
    result = int((error / count) * 100)
    print(result)