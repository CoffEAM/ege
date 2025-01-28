def f(b):
    for x in range(1000):
        f = (((x & 500) != 0) and (x & 200 == 0)) <= (not(x & b == 0))
        if not f:
            return 0
    return 1

for b in range(1000):
    if f(b):
        print(b)

