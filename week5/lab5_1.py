with open("input.txt", "r") as in_file:
	with open("output.txt", "w") as out_file:
		for line in in_file:
			out_file.write(line.upper())
