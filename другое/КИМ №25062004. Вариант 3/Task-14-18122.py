for x in range(1, 5556):
    num = 5**150 + 5**135 - x
    res = ''
    while num:
        res += str(num%5)
        num //= 5
    if res.count('4') == 134:
        print(x)

