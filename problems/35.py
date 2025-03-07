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
