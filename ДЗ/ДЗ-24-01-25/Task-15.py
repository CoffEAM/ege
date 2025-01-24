def plov(a, b, c):
    if (a*b) > c:
        return 1
    else:
        return 0

def f(A):
    for a in range(1, 10000):
        for b in range(1, 10000):
            f = (not(plov(a, b, A+13))) <= (plov(28, b, 520) or plov(a, 25, 800))
            if f:
                return 1
    return 0

print(plov(15, 17, 47))

for A in range(1, 100000):
    if not f(A):
        print(A)

