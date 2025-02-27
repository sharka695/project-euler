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

def d(n):
    divs = divisors(n)
    divs.remove(n)
    return sum(divs)

def sumOfAmicableNumbers():
    amicables = set()
    memo = dict()
    def d_memo(n):
        if n not in memo:
            memo[n] = d(n)
        return memo[n]
    for a in range(10_000):
        # b = d_memo(a)
        if d_memo(b:=d_memo(a)) == a and a != b:
            amicables.add(a)
            amicables.add(b)
    return sum(amicables) # 31_626
