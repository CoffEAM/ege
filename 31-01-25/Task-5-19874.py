def con(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]

arr = []
for n in range(10, 10000):
    r = con(n)
    if n%4 == 0:
        r += r[-3:]
    else:
        r = '1' + r +'20'
    r = int(r, 3)
    if r > 423:
        arr.append(r)
print(min(arr))


