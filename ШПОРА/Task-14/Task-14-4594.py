num = 4 * 625 ** 1920 + 4 * 125**1930 - 4 * 25**1940 - 3 * 5**1950 - 1960
res = ''
while num:
    res += str(num%5)
    num //= 5
print(res.count('0'))
