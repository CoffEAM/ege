def f(a):
    for x in range(1, 1000):
        f = ((x%7!=0) and (x%13==0)) <= (x > a - 40)
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)
