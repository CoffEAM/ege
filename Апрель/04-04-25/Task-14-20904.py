for x in range(2030, 1, -1):
    num = 3**100 - x
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    if res.count('0') == 1:
        print(x)
        break
