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

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

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

def primesLessThan(n):
    primes = set()
    primes.add(2)
    for i in range(3, n + 1, 2):
        primes.add(i)
    for i in range(3, n + 1, 2):
        for j in range(2, ((n + 1) // i) + 1):
            primes.discard(i * j)
    return primes

all_primes = primesLessThan(2_000_000)
sum(all_primes) # 142_913_828_922










def primesLessThan(n):
    primes = set()
    primes.add(2)
    for i in range(3, n + 1, 2):
        primes.add(i)
    for i in range(3, n + 1, 2):
        for j in range(2, ((n + 1) // i) + 1):
            primes.discard(i * j)
    return primes

def digitsOf(number, base=10):
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))

def digitsToNum(digits):
    total = 0
    for i in range(len(digits)):
        total += digits[-(i + 1)] * (10 ** i)
    return total

def rotations(n):
    digits = digitsOf(n)
    rotates = set()
    for i in range(len(digits)):
        rotates.add(digitsToNum(digits[i:] + digits[:i]))
    return rotates

def circularPrimes():
    primes = primesLessThan(1_000_000)
    circulars = set()
    for prime in primes:
        # Check if rotations are in primes. If so, put them in circulars set.
        rotates = rotations(prime)
        if all([(lambda n: n in primes)(rotate) for rotate in rotates]):
            circulars |= rotates
    return len(circulars) # 55
