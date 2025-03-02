def f(a):
    for x in range(1000):
        for y in range(1000):
            u = (x < 7) or (y >= 5*x + a - 60) or (x >= 36) or (y < 225)
            if not u:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
