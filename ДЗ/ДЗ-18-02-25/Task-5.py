def c(num):
    res = ''
    while num:
        res += str(num%4)
        num //= 4
    return res[::-1]

for n in range(1, 10000):
    r = c(n)
    if len(r)%2==0:
        r = r[:len(r)//2] + '0' + r[len(r)//2:]
    else:
        r = r
    r = int(r)
    if r <= 180:
        print(n)
