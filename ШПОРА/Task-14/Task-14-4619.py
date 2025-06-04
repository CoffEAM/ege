num = 343**1515 - 6 * 49**1520 + 5*49**1510 - 3 * 7**1530 - 1550
res = ''
while num:
    res += str(num%7)
    num //= 7
print(res.count('0'))
