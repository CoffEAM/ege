def con(num):
    res = ''
    while num:
        res += str(num%4)
        num //= 4
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = con(n)
    if n%4 == 0:
        r = '2' + r + '03'
    else:
        r = r + con((n%4)*5)
    r = int(r, 4)
    if r <= 567:
        ans.append(n)
print(max(ans))






