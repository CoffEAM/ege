minn = 1000
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += bin(n%3*3)[2:]
    r = int(r, 2)
    if 195 <= r <= minn:
        minn = min(minn, r)
print(minn)
