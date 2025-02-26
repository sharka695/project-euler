def factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def sumDigits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

sumDigits(factorial(100)) # 648
