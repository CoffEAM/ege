def f(A):
    for x in range(1000):
        for y in range(1000):
            f = (x**2 + y**2 > 1024-x) or (y < -2*x + A)
            if not f:
                return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
        break

