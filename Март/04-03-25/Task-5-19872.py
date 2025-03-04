def c(n):
    res = ''
    while n:
        res += str(n%7)
        n //= 7
    return res[::-1]

for n in range(1, 1000):
    r = c(n)
    if n%2==0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'
    r = int(r)
    if len(str(r)) == 4:
        print(n)
