minn = 150
for n in range(1, 10000):
    r = bin(n)[2:]
    r += str(sum(map(int, r)) % 2)
    r += str(sum(map(int, r)) % 2)
    r = int(r, 2)
    if 75 < r < minn:
        minn = r
print(minn)
