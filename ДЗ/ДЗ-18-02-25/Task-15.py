def f(a):
    for x in range(90, 101):
        f = (x&79!=0) and ((x&31==0) <= (x&a!=0))
        if not f:
            return 0
    return 1

for a in range(1000):
    if f(a):
        print(a)
        break
