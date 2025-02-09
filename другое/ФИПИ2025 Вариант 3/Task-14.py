for x in range(1, 1001):
    num = 6**2025 + 6**25 - x
    res = ''
    while num:
        res += str(num%6)
        num //= 6
    if res.count('0')==2002:
        print(x)

#972

