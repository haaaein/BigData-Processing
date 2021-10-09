dspam_sum = 0.0
dspam_count = 0;
with open("mbox-short.txt", "r") as in_file:
	for line in in_file:
		if line.startswith("X-DSPAM-Confidence"):
			#print(line.strip())
			str_arr = line.strip().split()
			dspam_sum += float(str_arr[1])
			dspam_count += 1
print(dspam_sum/dspam_count)
