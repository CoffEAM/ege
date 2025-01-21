def f(A):
    for x in range(1000):
        for y in range(1000):
            f = (2*x + y != 70) or (x < y) or (A < x)
            if not f:
                return False
    return True

for A in range(1000):
    if f(A):
        print(A)


