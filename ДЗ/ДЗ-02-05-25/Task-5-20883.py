def c(n):
    res = ''
    while n:
        res += str(n%5)
        n //= 5
    return res[::-1]

for n in range(1, 10000):
    r = c(n)
    if len(r) % 2 == 0:
        r = r[len(r)//2:] + r[:len(r)//2]
    else:
        r += str(n%5)
        r = r[len(r)//2:] + r[:len(r)//2]
    r = int(r, 5)
    if r > 50:
        print(n)
        break
