def d(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        if res[-1] % 7 == 0:
            return res[-1]
    return False

cnt = 0
for i in range(10**9, 10**12):
    if str(i) == str(i)[::-1]:
        u = d(i)
        if u:
            print(i, u)
            cnt += 1
            if cnt == 5:
                break
