for x in range(1, 2031):
    num = 3**100 - x
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    if res.count('0') == 5:
        print(x)
