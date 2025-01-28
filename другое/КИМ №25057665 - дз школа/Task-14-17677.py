for x in range(1, 2031):
    num = 6**260 + 6**160 + 6**60 - x
    res = ''
    while num:
        res += str(num%6)
        num //= 6
    if res.count('0') == 202:
        print(x)



