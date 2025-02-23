def cif(x, y):
    if str(x)[-1] == str(y)[-1]:
        return 1
    else:
        return 0


def f(a):
    for x in range(1, 1000):
        f = ((not (cif(x, 5)) and cif(x, 4))) <= (x > a - 11)
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)
