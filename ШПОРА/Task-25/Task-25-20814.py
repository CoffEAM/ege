def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        return sum(res)
    return 0

cnt = 0
for i in range(500001, 10**10):
    u = f(i)
    if str(u)[-1] == '9':
        print(i, u)
        cnt += 1
        if cnt == 5:
            break
