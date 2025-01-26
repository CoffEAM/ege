ans = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if sum(map(int, r))%2==0:
        r += '0'
        r = '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]
    r = int(r, 2)
    if n > 27:
        ans.append(r)
print(min(ans))


