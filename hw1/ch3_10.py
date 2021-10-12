list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b = []
for i in range(len(list_a)):
  if i % 2 != 1:
    list_b.append(list_a[i])
print(list_b)