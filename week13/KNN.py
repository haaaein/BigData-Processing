import numpy as np
import operator

def createDataSet():
  group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]) # 배열 생성 
  labels = ['A', 'A', 'B', 'B'] # 각 데이터와 매칭되는 라벨 리스트
  return group, labels

def autoNorm(dataSet):
  minVals = dataSet.min(0) # 집합에서의 최솟값. param 0은 column의 최솟값을 얻게 함 
  maxVals = dataSet.max(0) # 집합에서의 최댓값
  ranges = maxVals - minVals # 범위
  normDataSet = np.zeros(np.shape(dataSet))
  m = dataSet.shape[0]
  normDataSet = dataSet - np.tile(minVals, (m, 1)) # 행렬 크기 맞춰주기 
  normDataSet = normDataSet / np.tile(ranges, (m, 1)) # 구성요소 나누기
  return normDataSet, ranges, minVals

#Putting the K-NN classification algorithm into action
def classify0(inX, dataSet, labels, k):
  # 거리 계산 (Euclidian distance)
  dataSetSize = dataSet.shape[0]
  diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
  sqDiffMat = diffMat ** 2
  sqDistances = sqDiffMat.sum(axis = 1) # 주어진 axis로 배열 요소들의 합계 반환 
  distances = sqDistances ** 0.5
  sortedDistIndicies = distances.argsort() # 배열 소팅 후 인덱스 반환 
  classCount = {}
  for i in range(k): # 가장 짧은 거리를 투표
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
  sortedClassCount = sorted(classCount.items(), 
      key = operator.itemgetter(1), reverse = True) # 아이템 정렬
  return sortedClassCount[0][0]

if __name__ == "__main__":
  group, labels = createDataSet() 
  print("group\n", group)
  print("labels = ", labels) 
  print(classify0([0, 0], group, labels, 3))

