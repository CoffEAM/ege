def c(n):
    res = ''
    while n:
        res += str(n%3)
        n //= 3
    return res[::-1]

for n in range(1, 10000)[::-1]:
    r = c(n)
    if n % 5 == 0:
        r += r[-3:]
    else:
        r += c((n%5)*5)
    r = int(r, 3)
    if r < 5496:
        print(n)
        break
