def d(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    s = []
    if res:
        for num in res:
            if str(num)[-1] == '7' and num != 7:
                s.append(num)
        if s:
            return min(s)
        return False
    return False

cnt = 0
for i in range(1125001, 10**10):
    u = d(i)
    if u:
        cnt += 1
        print(i, u)
        if cnt == 5:
            break
