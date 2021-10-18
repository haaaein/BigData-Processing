def count_ones(n):
  count = 0
  for i in range(1, n + 1):
    for j in str(i):
      if '1' in j:
        count += 1
  return count

num = int(input("Enter a number: " ))
print(count_ones(num))
