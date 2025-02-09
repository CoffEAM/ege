def f(a):
    for x in range(1, 1000):
        b = 200 <= x <= 300
        f = (x%a==0) or (b <= (x%77!=0))
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)
#231

