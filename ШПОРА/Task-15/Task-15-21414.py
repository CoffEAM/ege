def f(a):
    for x in range(1000):
        for y in range(1000):
            u = (5 < y) or (x > 32) or (x + 2 * y < a)
            if not u:
                return False
    return True

for a in range(1000):
    if f(a):
        print(a)
        break
