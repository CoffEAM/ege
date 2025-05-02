for n in range(4, 10000):
    r = bin(n)[2:]
    cnt_1 = r.count('1')
    cnt_0 = r.count('0')
    if cnt_1 > cnt_0:
        r += '0'
    else:
        r += '1'
    if len(r) % 2 == 0:
        r = r[:len(r)//2 - 1] + r[len(r)//2 + 1:]
    else:
        r = r[:len(r)//2 - 1] + r[len(r)//2 + 2:]
    r = int(r, 2)
    if r == 55:
        print(n)
        break
