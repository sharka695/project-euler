def pythagorean(a, b):
    return (a * a) + (b * b)

def isPythagoreanTriplet(a, b, c):
    return pythagorean(a, b) == (c * c)

def findPythagoreanTriplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a + b + c == 1000 and isPythagoreanTriplet(a, b, c):
                    print(a, b, c) # 200 375 425
                    return a * b * c # 31875000

findPythagoreanTriplet()
