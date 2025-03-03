def div(n, d):
    def strung(q, fractional):
        fractional = map(str, fractional)
        return str(q) + "".join(fractional)
    q = n // d
    r = n % d
    fractional = []
    r_to_diff = dict()
    while r != 0:
        for k in range(10):
            if d * k > r * 10:
                fractional.append(k - 1)
                diff = (r * 10) - (d * k)
                if r not in r_to_diff:
                    r_to_diff[r] = set()
                    r_to_diff[r].add(diff)
                elif diff not in r_to_diff[r]:
                    r_to_diff[r].add(diff)
                else:
                    return strung(q, fractional)
                r = diff
                break
            elif d * k == r * 10:
                fractional.append(k)
                break
        print(q, r, fractional)
    return strung(q, fractional)
