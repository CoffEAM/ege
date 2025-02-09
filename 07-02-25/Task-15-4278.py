def f(a):
    for x in range(1, 1000):
        f= (a%12==0) and ((530%x==0) <= ((not(a%x==0)) <= (not(170%x==0))))
        if not f:
            return 0
    return 1

cnt = 0
for a in range(1, 1001):
    if f(a):
        cnt += 1
print(cnt)


