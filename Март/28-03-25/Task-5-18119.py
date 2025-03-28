def c(n):
    res = ''
    while n:
        res += str(n%3)
        n //= 3
    return res[::-1]


ans = []
for n in range(1, 10000):
    r = c(n)
    suum = sum(map(int, r))
    if suum%2==0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'
    r = int(r, 3)
    if r > 100:
        ans.append(r)
print(min(ans))
