def delet(n, m):
    return 1 if n%m==0 else 0

def f(a):
    for x in range(1, 51*3):
        for y in range(1, 78*3):
            for z in range(1, 115*3):
                f = (delet(z, 115) or delet(y, 78) or delet(x, 51)) <= delet(x, a)
                if not f:
                    return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)


