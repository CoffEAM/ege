def f(A):
    for x in range(1000):
        for y in range(1000):
            f = (x + 2*y > A) or (y < x) or (x < 30)
            if not f:
                return 0
    return 1
for A in range(1000):
    if f(A):
        print(A)


