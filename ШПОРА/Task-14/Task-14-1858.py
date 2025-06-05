num = 4 * 625**9 - 25**15 + 2 * 5 ** 11 - 7
res = ''
while num:
    res += str(num % 5)
    num //= 5
print(res.count('4'))
