for x in range(1, 2006)[::-1]:
    num = 43 ** 56 + 113 ** 841 - x
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    u1 = sum(1 for i in res if i in '02') % 2 == 0
    u2 = sum(1 for i in res if i in '13') % 2 == 0
    u3 = res.count('2') <= 712
    if u1 and u2 and u3:
        print(x)
        break
