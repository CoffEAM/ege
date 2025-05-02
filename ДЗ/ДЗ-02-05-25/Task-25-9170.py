def d(num):
    res = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num//i}
    res = sorted(res)
    k = [i for i in res if fnmatch(str(i), '4*')]
    if len(k) == 24:
        return k[-1]
    return False

from fnmatch import fnmatch

for i in range(100, 10**6):
    u = d(i)
    if u:
        print(i, u)
