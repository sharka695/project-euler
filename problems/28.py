def numberSpiralDiagonals(n):
    if n % 2 == 0 or n < 1:
        return -1
    total = 0
    for i in range(1, n + 1, 2):
        if i == 1:
            total += 1
            continue
        diff = i - 1
        upper_right = i * i
        upper_left = upper_right - diff
        lower_left = upper_left - diff
        lower_right = lower_left - diff
        total += upper_right + upper_left + lower_left + lower_right
    return total

numberSpiralDiagonals(5) == 101
numberSpiralDiagonals(1001) # 669_171_001
