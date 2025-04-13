from fnmatch import fnmatch

def d(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) == 18:
        return max(res)
    return False

ans = []
for i in range(12045, 10**7+1):
    if fnmatch(str(i), '12?*45'):
        u = d(i)
        if u:
            ans.append([i, u])
for i in ans:
    print(*i)
