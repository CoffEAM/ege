def f(num):
    res = set()
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            res |= {i, num//i}
    res = sorted(res)
    summ = sum(res)
    comb = 1
    for i in res:
        comb *= i
    if summ%2==1 and comb%2==1:
        if len(res)>10:
            return len(res)
    return 0

cnt = 0
for i in range(800001, 10**10):
    u = f(i)
    if u:
        print(i, u)
        cnt += 1
        if cnt == 6:
            break
