import sys

sys.argv[0] = input_path
sys.argv[1] = output_path

result = dict()

with open(input_path, 'r') as file:
  for s in file:
    words = s.strip().split("::")
    genres = words[2].split("|")
    for genre in genres:
      if genre not in result:
        result[genre] = 1
      else:
        result[genre] += 1

i = 0
output = []
result_list = list(zip(result.keys(),result.values())) 

length = len(result_list)
for i in range(length):
  tmp = ""
  title = result_list[i][0]
  count = result_list[i][1]
  count_str = "{}".format(count)
  tmp = title + " " + count_str
  output.append(tmp)

f = open(output_path, 'w')
for out in output:
    f.write(out + "\n")
f.close()
