def f(a):
    for x in range(1, 1000):
        f =((x&17!=0) <= ((x&a!=0) <= (x&58!=0))) <= ((x&8==0) and (x&a!=0) and (x&58==0))
        if f:
            return 0
    return 1

for a in range(43, 56):
    if f(a):
        print(a)


