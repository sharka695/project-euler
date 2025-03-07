""" Dynamic programming offers a very nice way to quickly calculate Fibonacci numbers by
    calculating each Fibonacci number only once, using the results of only the previous two
    calculations, each stored in a variable (a and b).

    While calculating each Fibonacci number, one can filter for even-ness by dividing it by 2,
    checking if the remainder is 0, then adding it to the total if it's even (i.e., n is even if n mod 2 = 0).
"""

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
