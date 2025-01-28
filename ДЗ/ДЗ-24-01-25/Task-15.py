def plov(a, b, c):
    if a*b > c:
        return True
    else:
        return False

def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (not(plov(x, y, a+13))) <= (plov(28, y, 520) or plov(x, 25, 800))
            if not f:
                return 0
    return 1

for a in range(-1000, 1000):
    if f(a):
        print(a)




