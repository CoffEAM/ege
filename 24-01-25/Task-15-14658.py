def delet(n,m):
    if n%m==0:
        return 1
    else:
        return 0

def f(a):
    for x in range(1, 1000):
        f = (delet(x, 12) <= (not(delet(x, 42)))) or (x + a >= 4096)
        if not f:
            return 0
    return 1

for a in range(1, 5000):
    if f(a):
        print(a)
        break


