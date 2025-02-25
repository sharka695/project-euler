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

def highlyDivisibleTriangularNumber(num_divisors):
    i = 1
    ith_triangle_number = i
    while len(divisors(ith_triangle_number)) <= num_divisors:
        # print(ith_triangle_number)
        i += 1
        ith_triangle_number += i
    return ith_triangle_number # 76_576_500
