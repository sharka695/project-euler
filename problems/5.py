def factor(n):
    factor = 2
    factors = set()
    while factor <= n:
        while n % factor == 0:
            factors.add(factor)
            n //= factor
        factor += 1
    return factors

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

# def findSmallestMultiple():
#     factors = set()
#     for i in range(21):
#         factors = factors | factor(i)
#     print(factors)
#     product = 1
#     for multiplier in factors:
#         product *= multiplier
#     return product


def findSmallestMultiple(n):
    factors = dict()
    for i in range(n + 1):
        factorization, total = uniqueFactorization(i)
        for factor, exponent in factorization.items():
            if factor in factors:
                factors[factor] = factors[factor] if factors[factor] >= exponent else exponent
            else:
                factors[factor] = exponent
    print(factors)
    product = 1
    for factor, exponent in factors.items():
        product *= factor ** exponent
    return product

def divideNByNums(n, nums):
    for num in nums:
        print(n % num)

divideNByNums(232792560, [i for i in range(1, 21)])
