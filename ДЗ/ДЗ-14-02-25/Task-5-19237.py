def c(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = c(n)
    if n%3==0:
        r += r[-2:]
    else:
        r += c(sum(map(int, r)))
    r = int(r, 3)
    if r > 220 and r%2==0:
        ans.append(r)
print(min(ans))
