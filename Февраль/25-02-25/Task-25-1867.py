def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            res |= {i, num // i}

    res = sorted(res)
    for i in res:
        if i%10==8 and i != 8:
            return i
    return 0

cnt = 0
for i in range(500001, 10**20):
    u = f(i)
    if u:
        print(i, u)
        cnt += 1
        if cnt == 5:
            break
