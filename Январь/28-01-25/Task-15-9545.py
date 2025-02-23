def delet(x, d):
    if x%d==0:
        return 1
    else:
        return 0

def f(a):
    for x in range(1, 1000):
        f = (delet(x, 10) and delet(x, 26) and (x >= 300)) <= (a <= x)
        if not f:
            return 0
    return 1

for a in range(1, 10000):
    if f(a):
        print(a)


