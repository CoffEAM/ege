def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x+y<=24) or (y <= x-2) or (y >= a)
            if not f:
                return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)



