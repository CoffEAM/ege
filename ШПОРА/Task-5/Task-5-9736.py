ans = 0
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin(n%3*3)[2:]
    r = int(r, 2)
    if r <= 170:
        ans = max(r, ans)
print(ans)
