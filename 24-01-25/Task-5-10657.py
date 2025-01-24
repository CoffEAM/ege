def con(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]

for n in range(1, 10000):
    r = con(n)
    if sum(map(int, r))%3==0:
        r = '20' + r
    else:
        r = '10' + r
    r = int(r, 3)
    if r<100:
        print(n)


