def f(a):
    for x in range(1, 1000):
        u = ((x&52!=0) and (x&36==0)) <= (not(x&a==0))
        if not u:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)
        break
