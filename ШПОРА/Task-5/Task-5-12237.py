for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += r[-2:]
    else:
        r = '1' + r + '0'
    r = int(r, 2)
    if r < 100:
        print(n)
