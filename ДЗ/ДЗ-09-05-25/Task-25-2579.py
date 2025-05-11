def d(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) >= 3:
        return sum(res[-3:])
    return 0

cnt = 0
for i in range(10000001, 10**15):
    u = d(i)
    if u ** 0.5 == int(u ** 0.5) and u ** 0.5 != 0:
        print(u)
        cnt += 1
        if cnt == 5:
            break
