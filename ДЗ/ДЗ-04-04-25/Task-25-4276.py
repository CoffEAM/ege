def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res, reverse=True)
    if len(res) >= 7:
        dn = res[6]
    else:
        dn = 0
    if dn:
        return [dn, len(res)]
    return 0

ans = []
cnt = 0
for i in range(400_000_001, 10**10):
    u = f(i)
    if u:
        ans.append([u[0], u[1]])
        cnt += 1
        if cnt == 5:
            break

for i in ans:
    print(*i)
