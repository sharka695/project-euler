""" Rather than writing a function to find the sum of the multiples of both 3 and 5 under 1,000,
    one can sum up the multiples of each, then subtract the sum of the multiples of both.
    This accounts for the numbers counted twice (e.g., 30 will be counted in both sums, so it should be removed once).
"""

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
