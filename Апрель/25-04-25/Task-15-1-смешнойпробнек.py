def f(a):
    for x in range(100000):
        u = ((x & 8375 != 0) or (x & 6743 != 0)) <= (x & a > 0)
        if not u:
            return False
    return True

for a in range(1, 50000):
    if f(a):
        print(a)
        break
