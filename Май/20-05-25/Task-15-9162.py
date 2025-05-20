def p(a, b, c):
    return a * b > c

def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            u = (not(p(x, y, a + 13))) <= (p(28, y, 520) or p(x, 25, 800))
            if not u:
                return False
    return True

for a in range(-10000, 10000)[::-1]:
    if f(a):
        print(a)
        break
