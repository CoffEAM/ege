minn = 10000
for n in range(28, 10000):
    r = bin(n)[2:]
    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    r = int(r, 2)
    minn = min(r, minn)
print(minn)
