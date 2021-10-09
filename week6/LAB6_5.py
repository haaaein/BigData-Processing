import json

with open('movies.json') as datafile:
  jsondata = json.load(datafile)

movies = list(jsondata['boxOfficeResult']['dailyBoxOfficeList'])

sum = 0
for movie in movies:
  sum += int(movie['salesAmt'])

print("오늘 매출액은 총 ", sum, "원")
