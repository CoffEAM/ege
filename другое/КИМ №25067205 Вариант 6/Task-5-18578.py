def c(n):
    res = ''
    while n:
        res += str(n%4)
        n //= 4
    return res[::-1]

for n in range(1, 10000):
    r = c(n)
    if n%4==0:
        r = '2' + r + '03'
    else:
        r += c(5*(n%4))
    r = int(r, 4)
    if r <= 567:
        print(n)
