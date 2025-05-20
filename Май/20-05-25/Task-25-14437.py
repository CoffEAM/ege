def d(num):
    res = set()
    for i in range(2, int(num** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        return int(sum(res)/len(res))
    return 0

cnt = 0
for i in range(700000, 0, - 1):
    m = d(i)
    if str(m)[-3:] == '313':
        print(i, m)
        cnt += 1
        if cnt == 7:
            break
