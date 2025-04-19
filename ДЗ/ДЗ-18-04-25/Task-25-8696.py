def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if not res:
        return 0
    else:
        return sum(res)

ans = []
cnt = 0
for i in range(1273548, 10**20):
    u = f(i)
    if u:
        if not f(u % 100000):
            ans.append([i, u])
            cnt += 1
            if cnt == 5:
                break

for i in ans:
    print(*i)
