upper_limit = 28_123

def divisors(n):
    result = set()
    if n <= 1:
        result.add(n)
        return result
    i = 1
    while i not in result:
        if n % i == 0:
            result.add(i)
            result.add(n // i)
        i += 1
    return result

def evaluatePerection(n):
    divs = divisors(n)
    divs.remove(n)
    return sum(divs)

def isPerfect(n):
    return evaluatePerection(n) == n

def isDeficient(n):
    return evaluatePerection(n) < n

def isAbundant(n):
    return evaluatePerection(n) > n

