def make_new_list(listA):
  B = []
  for i in listA:
    num = 1
    for j in listA:
      if j != i:
        num *= j
    B.append(len(str(num)))
  return B

listA = list(map(int, input('숫자들을 입력하세요.(각 값은 공백으로 분리):').split()))
print(make_new_list(listA))