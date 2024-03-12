seen = [1, 2, 3]
prod = [1, 2, 3]
for x in range(4, 11):
  if x not in seen:
    for y in seen:
      if x % y == 0:
        prod.append(x % y)

print(prod)