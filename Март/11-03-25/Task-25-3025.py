def f(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i==0:
            res |= {i, num//i}
    res = sorted([i for i in res if i%2==1], reverse=True)
    if len(res)<6:
        d = 0
    else:
        d = res[5]
    return d

ans = []
cnt = 0
for i in range(200000001, 10**20):
    u = f(i)
    if u:
        ans.append([i, u])
        cnt += 1
        if cnt == 5:
            break
for i in ans:
    print(*i)

