def con(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = con(n)
    if sum(map(int, r))%3==0:
        r += '212'
    else:
        r += con((sum(map(int, r))) * 2)
    r = int(r, 3)
    if r >490:
        ans.append(r)
print(min(ans))


