def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (y > 10) or (x*a > y + x)
            if not f:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
        break


