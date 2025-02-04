for x in range(1, 1000):
    num = 7**666 + 7**333 + 49**x - 343
    res = ''
    while num:
        res += str(num%7)
        num //= 7
    if res.count('6')==49:
        print(x)
        break
