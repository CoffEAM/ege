for n in range(1, 10000):
    r = bin(n)[2:]
    r1 = r.replace('0', '1')
    r2 = r.replace('1', '0')
    r = r1 + r2
    if r.count('1') % 2 == 0:
        r += '0'
    else:
        r += '1'
    r = int(r, 2)
    if r > 180:
        print(n)
        break
