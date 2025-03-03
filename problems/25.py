def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

def digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def nDigitFib(n=1_000):
    a, b = 1, 1
    index = 1
    while digits(a) < 1_000:
        a, b = b, a + b
        index += 1
    return index # 4782
