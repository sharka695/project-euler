""" Factorization can be done by dividing the number by candidate factors. If there's no remainder,
    then the candidate is a factor. This factor can then be "removed" from the number by division.
    Doing so repeatedly yields a unique prime factorization, in keeping with the fundamental theorem of arithmetic.
    Given the unique prime factorization, one can find the largest factor by comparing each prime. If they're small
    enough, you might just be able to compare them by looking at them. You can also use the max function, which will do
    this comparison for you.
"""

num = 600_851_475_143
def uniqueFactorization(n):
    factor = 2
    factors = dict()
    total = 0
    while factor <= n:
        while n % factor == 0:
            if factor not in factors:
                factors[factor] = 0
            factors[factor] += 1
            n //= factor
            total += 1
        factor += 1
    return factors, total

uniqueFactorization(num)
