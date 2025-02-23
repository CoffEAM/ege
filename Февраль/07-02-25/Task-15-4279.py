def f(a):
    for x in range(1, 1000):
        f = (x&1097==0) <= ((x&2047!=0) <= (x&a!=0))
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)
        break


