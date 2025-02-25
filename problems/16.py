num = 2 ** 1000

def digitsOf(number, base=10):
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))

digits = digitsOf(num)
sum(digits) # 1366
