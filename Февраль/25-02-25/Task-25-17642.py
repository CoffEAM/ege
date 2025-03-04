def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            res |= {i, num // i}
    res = sorted(res)
    for i in res:
        if str(i)[-1] == '9' and i != 9:
            return i
    return 0

cnt = 0
for i in range(800001, 10**10):
    u = f(i)
    if u:
        print(i, u)
        cnt += 1
        if cnt == 5:
            break
