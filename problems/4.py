""" I had a few false starts with this, and ended up just going with a brute-force answer,
    going through all of the products of two three-digit numbers and finding the biggest one
    that is also a palindrome. Turning a number into a string and checking if the string is
    a palindrome is a straightforward approach, but sometimes it's fun to work more closely
    with integers directly. The results are the same, and used an array anyways, but it is
    what it is. Taking the log, base 10, of a number, then taking its floor, would have
    yielded the length of the number, which could have then been used to compare each digit
    without an array. There's probably other ways to check palindromicity as well, but the
    approach worked.
"""

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

def isPalindrome(n):
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    return True

def digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def allThreeDigit(nums):
    for num in nums:
        if digits(num) != 3:
            return False
    return True

# def largestPalindromeFromThreeDigitFactors():
#     for i in range((1000 * 1000), (100 * 100), -1):
#         if isPalindrome(i):
#             factors, total = uniqueFactorization(i)
#             if total == 2:
#                 #if allThreeDigit(factors.keys()):
#                 print(i, uniqueFactorization(i))
#                     #return i, uniqueFactorization(i)

def palindromeFromThreeDigitPair(n):
    if not isPalindrome(n):
        return {}, 0
    factor = 2
    factors = dict()
    total = 0
    while factor <= n:
        while n % factor == 0:
            if digits(factor) == 3:
                if factor not in factors:
                    factors[factor] = 0
                factors[factor] += 1
            else:
                return {}, 0
            n //= factor
            total += 1
            # if total > 2:
            #     return {}, 0
        factor += 1
    return factors, total


def largestPalindromeFromThreeDigitFactors():
    for i in range((1000 * 1000), (100 * 100), -1):
        factors, total = palindromeFromThreeDigitPair(i)
        if factors:
            print(i, factors, total)


def largestPalindromeFromThreeDigitFactors():
    for i in range((1000 * 1000), (100 * 100), -1):
        if not isPalindrome(i):
            continue
        factors = factor(i)
        if allThreeDigit(factors):
            print(i, factors)

def checkForRest():
    for i in range(353, 1000):
        for j in range(283, 1000):
            product = i * j
            if isPalindrome(product):
                print(product)

def findFirst():
    biggest = 0
    big_i = 0
    big_j = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if isPalindrome(product):
                if product > biggest:
                    biggest = product
                    big_i, big_j = i, j
    print(big_i, big_j)
    return biggest
