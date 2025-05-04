def d(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        return sum(res)
    return 0

cnt = 0
for i in range(500000, 10**10):
    u = d(i)
    if str(u)[-1] == '9':
        cnt += 1
        print(i, u)
        if cnt == 5:
            break
