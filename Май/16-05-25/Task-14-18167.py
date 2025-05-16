for x in range(1, 10001)[::-1]:
    num = 6 ** 900 + 6 ** 10 - x
    res = ''
    while num:
        res += str(num % 6)
        num //= 6
    if res.count('3') == res.count('5'):
        print(x)
        break
