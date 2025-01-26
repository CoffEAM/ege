def f(a):
    for x in range(1000):
        for y in range(1000):
            f = not((x<7) or (y >= 3*x + a - 20) or (x >= 34) or (y < 121))
            if f:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)


