def is_prime(num):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    return True if len(res) == 2 else False

def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        u = [i for i in res if is_prime(i)]
        if u:
            return sum(u)
    return 0

cnt = 0
for i in range(32500000, 10**12):
    u = f(i)
    if u != 0 and u % 145 == 0:
        print(i, u)
        cnt += 1
        if cnt == 7:
            break
