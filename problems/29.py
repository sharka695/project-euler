def distinctPowers(n):
    terms = set()
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            terms.add(a ** b)
    return len(terms)

distinctPowers(100) # 9183
