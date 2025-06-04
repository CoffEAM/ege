def f(a):
    for x in range(1, 1000):
        b = 60 <= x <= 80
        u = (x % a == 0) or (b <= (x % 22 != 0))
        if not u:
            return False
    return True

for a in range(1, 1000):
    if f(a):
        print(a)
