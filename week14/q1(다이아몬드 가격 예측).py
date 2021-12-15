import numpy as np
def loadDataSet(filename):
  priceMat = []; caratMat = [];
  with open(filename) as f:
    for line in f:
      if line.startswith("Price"): #첫줄은 메타데이터 이므로 무시
        continue
      instance = str.strip(line).split('\t')
      priceMat.append(float(instance[0]))
      caratMat.append([1.0, float(instance[1])])
  return caratMat, priceMat

def standRegres(xArr, yArr):
  xMat = np.mat(xArr); yMat = np.mat(yArr).T # 각 배열을 행렬로 변환 
  xTx = xMat.T * xMat # X와 X의 전치행렬을 곱함
  if np.linalg.det(xTx) == 0.0: # 0이면 역행렬 계산이 불가능
    print('This matrix is singular, cannot do inverse')
    return
  ws = xTx.I * (xMat.T * yMat) 
  return ws # 계산한 가중치 반환

xArr, yArr = loadDataSet('diamonds.txt') 
ws = standRegres(xArr, yArr)

xMat = np.mat(xArr)
yHat = xMat * ws

print(ws)
print("x = ", xArr[10][1], ", calc val = ", yHat[10], ", real val = ", yArr[10]) 
print("x = ", xArr[1000][1], ", calc val = ", yHat[1000], ", real val = ", yArr[1000]) 
print("x = ", xArr[2300][1], ", calc val = ", yHat[2300], ", real val = ", yArr[2300])