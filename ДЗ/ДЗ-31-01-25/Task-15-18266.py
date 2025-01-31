def f(a):
    for x in range(1, 1000):
        f = (x & 57 == 0) or ((x & 23 == 0) <= (not(x & a == 0)))
        if not f:
            return 0
    return 1

for a in range(1, 10000):
    if f(a):
        print(a)
        break


