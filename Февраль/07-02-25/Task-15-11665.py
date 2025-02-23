def f(a):
    for x in range(1, 1000):
        f = (a + x > 700 - a) and (a%100 + 100%x > 50)
        if not f:
            return 0
    return 1

for a in range(1,1000):
    if f(a):
        print(a)
        break


