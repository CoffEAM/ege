def c(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]

minn = 200
for n in range(1, 10000):
    r = c(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += c(n%3*5)
    r = int(r, 3)
    if 133 < r < minn:
        minn = min(r, minn)
print(minn)
