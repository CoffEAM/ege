def f(a):
    for x in range(1000):
        for y in range(1000):
            u = not ((x < 7) or (y >= 3 * x + a - 20) or (x >= 34) or (y < 121))
            if u:
                return False
    return True

for a in range(5000, 1, -1):
    if f(a):
        print(a)
        break
