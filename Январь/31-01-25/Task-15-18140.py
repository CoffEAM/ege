def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - y >= 39) or (y <= x) or (y >= a - 20)
            if not f:
                return 0
    return 1

print(max(a for a in range(1000) if f(a)))



