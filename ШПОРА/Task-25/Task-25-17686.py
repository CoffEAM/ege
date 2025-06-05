def d(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        minn = [i for i in res if str(i)[-1] == '7' and i != 7]
        if minn: return min(minn)
    return 0

cnt = 0
for i in range(700001, 10**10):
    u = d(i)
    if u:
        print(i, u)
        cnt += 1
        if cnt == 5:
            break
