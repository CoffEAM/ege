def con(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
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


