def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res):
        M = res[0] + res[-1]
        if M%10 == 4:
            return M
    return 0

cnt = 0
for i in range(800001, 10**20):
    u = f(i)
    if u:
        print(i, u)
        cnt += 1
        if cnt==5:
            break
