sender_hist  = dict()
with open("mbox-short.txt", "r") as in_file:
  for line in in_file:
    if line.startswith( "From:" ):
      #print(line.strip())
      str_arr = line.strip().split()
      if str_arr[1] not in sender_hist:
        sender_hist[str_arr[1]] = 1
      else:
        sender_hist[str_arr[1]] += 1

print( sender_hist )
