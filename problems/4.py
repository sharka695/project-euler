def factor(n):
    factor = 2
    factors = set()
    while n:
      while n % factor == 0:
        factors.add(factor)
        n // = factor
      factor += 1
    return factors

def isPalindrome(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    i = 0
    j = len(digits) - 1
    while i < j
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    return True

for i in range((1000 * 1000), (100 * 100), -1):
    if isPalindrome(i) and len(factor(i)) > 1:
        return i
