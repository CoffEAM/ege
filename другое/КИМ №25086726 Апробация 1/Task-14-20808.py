maax = 73
for x in range(1, 2031):
    num = 7 ** 170 + 7 ** 100 - x
    res = ''
    while num:
        res += str(num%7)
        num //= 7
    if res.count('0') == 73:
        print(x)
