def f1(num):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) == 2:
        return True
    return False


def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and f1(i) and f1(num // i):
            res |= {i, num // i}
    res = sorted(res)
    if not res:
        s = 0
    else:
        s = sum(res)
    if s != 0 and s % 145 == 0:
        return s
    return False


ans = []
cnt = 0
for num in range(32500000, 2**30):
    u = f(num)
    if u:
        ans.append([num, u])
        cnt += 1
        if cnt == 7:
            break

for i in ans:
    print(*i)
