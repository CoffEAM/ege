def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x - 3*y < a) or (y > 400) or (x > 56)
            if not f:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
        break



