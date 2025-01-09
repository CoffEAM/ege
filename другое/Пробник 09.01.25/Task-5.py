def con(x):
    res = ''
    while x:
        res += str(x%3)
        x //= 3
    return res[::-1]

ans = []
for n in range(11, 10000):
    r = con(n)
    if r.count('2')+r.count('0') > r.count('1'):
        r = '22' + r
    else:
        r = '11' + r
    r = int(r, 3)
    if r > 100:
        ans.append(r)
print(min(ans))


