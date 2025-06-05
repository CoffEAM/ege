for x in range(1, 2031):
    num = 7**91 + 7**160 - x
    res = ''
    while num:
        res += str(num%7)
        num //= 7
    if res.count('0') == 70:
        print(x)
