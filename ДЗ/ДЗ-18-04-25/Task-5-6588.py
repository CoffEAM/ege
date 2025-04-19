for n in range(1, 10000):
    r = bin(n)[2:]
    res = '1'
    for i in r:
        if i == '1':
            res += '0'
        else:
            res += '1'
    r = res
    if r.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)
    if r > 180:
        print(n)
        break
