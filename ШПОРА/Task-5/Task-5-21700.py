def c(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]

for n in range(3, 10000):
    r = c(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += c(n%3*3)
    r = int(r, 3)
    if r <= 150:
        print(n)
