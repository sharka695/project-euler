def fib(n):
  a, b = 1, 2
  for i in range(n - 1):
    a, b = b, a + b
  return a

def even_fib_sum(n):
  a, b = 1, 2
  total = 0
  for i in range(n - 1):
    a, b = b, a + b
    if a % 2 == 0:
      total += a
  return total

def even_fib_sum_to(n = 4_000_000):
  a, b = 1, 2
  total = 0
  while a <= n:
    if a % 2 == 0:
      total += a
    a, b = b, a + b
  return total
print(even_fib_sum_to())
