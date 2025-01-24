def plov(a, b, c):
    if (a*b) > c:
        return 1
    else:
        return 0

def f(A):
    for x in range(1, 100000):
        for y in range(1, 100000):
            f = (not(plov(x, y, A+13))) <= (plov(28, y, 520) or plov(x, 25, 800))
            if not f:
                return 0
    return 1

for A in range(1000000):
    if f(A):
        print(A)

