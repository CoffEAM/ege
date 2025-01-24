def treygol(n,m,k):
    if n+m>k and n+k > m and m+k > n:
        return 1
    else:
        return 0

def maxx(a, b):
    if a > b:
        return a
    else:
        return b

def f(a):
    for x in range(1, 1000):
        f = treygol(a, 7,x) <= ((maxx(x+5, 14) <= 27) == (not(treygol(36, 21,x))))
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)

