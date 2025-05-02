def d(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    cnt = sum(1 for i in res if i in u)
    if cnt >= 20:
        suum = sum(i for i in res if i not in u)
        if suum:
            return suum
        else:
            return '0'
    return False


u = [2**i for i in range(1, 50)]
cnt = 0
for i in range(10**6, 10**12+1):
    if i % 2 == 0:
        y = d(i)
        if y:
            print(i, y)
            cnt += 1
            if cnt == 5:
                break
