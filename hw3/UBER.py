#!/usr/bin/pyton3

import sys
import datetime
import time

input_path = sys.argv[1] 
output_path = sys.argv[2] 

def getDay_c(a,b,c):
    daylist = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
    return daylist[datetime.date(a,b,c).weekday()]

result = dict()
with open(input_path, 'r') as file:
  for s in file:
    words = s.strip().split(",")
    region = words[0]
    date = words[1]
    vehicles = words[2]
    trips = words[3]

    tmp = date.split("/")
    m = int(tmp[0])
    d = int(tmp[1])
    y = int(tmp[2])

    day = getDay_c(y, m, d)

    key = region + "," + day

    if key not in result:
      result[key] = vehicles + "," + trips
    else:
      data = result[key]
      data_split = data.strip().split(",")
      v = int(data_split[0])
      t = int(data_split[1])

      v += (int(vehicles))
      t += (int(trips))

      result[key] = str(v) + "," + str(t)

result_list = list(zip(result.keys(),result.values())) 

f = open(output_path, 'w')
for r in result_list:
  f.write(r[0] + " " + r[1] + "\n")
f.close()



