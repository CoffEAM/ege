def c(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]

for n in range(1, 10000):
    r = c(n)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += c((n%3)*4)
    r = int(r, 3)
    if r < 199:
        print(n)
