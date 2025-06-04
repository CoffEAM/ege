maxx = 105
for x in range(1, 3001):
    num = 4 ** 210 + 4 ** 110 - x
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    if res.count('0') == maxx:
        print(x)
        break
