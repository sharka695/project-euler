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

def primes(n):
    results = []
    i = 2
    while len(results) < n:
        factors, total = uniqueFactorization(i)
        if total == 1:
            results.append(i)
        i += 1
    return results

def nth_prime(n):
    count = 0
    i = 2
    while count < n:
        factors, total = uniqueFactorization(i)
        if total == 1:
            count += 1
        i += 1
    return i - 1

print(nth_prime(10_001)) # 104_743
