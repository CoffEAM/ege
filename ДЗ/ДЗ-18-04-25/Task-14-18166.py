maax = 199
for x in range(3, 2025)[::-1]:
    num = 5 ** 2025 + 5 ** 200 - x
    res = ''
    while num:
        res += str(num % 5)
        num //= 5
    if res.count('4') == maax:
        print(x)
        break
