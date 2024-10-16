def sum_multiples_of(a, n):
  total = 0
  i = 1
  multiple = i * a
  while multiple < n:
    total += multiple
    i += 1
    multiple = i * a
  return total
print(sum_multiples_of(3,1000) + sum_multiples_of(5,1000) - sum_multiples_of(15,1000))
