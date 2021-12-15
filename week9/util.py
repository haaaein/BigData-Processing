INCH = 2.54 # 변수 정의

def calcsum(n): # 함수 정의
  sum = 0
  for num in range(n + 1):
    sum += num
  return sum

#조건문으로 테스트 코드를 감싸자
if __name__ == "__main__": #단독으로 실행되고 있을 때 true
  print("인치 = ", INCH)
  print("합계 = ", calcsum(10))
