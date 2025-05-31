def c(n):
    res = ''
    while n:
        res += str(n % 7)
        n //= 7
    return res[::-1]

for n in range(1, 10000)[::-1]:
    r = c(n)
    if r.count('2') % 2 == 0:
        r += '555'
    else:
        r = '1' + r
    r = int(r, 7)
    if r < 3799:
        print(n)
        break
