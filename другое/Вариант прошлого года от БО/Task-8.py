from itertools import product

ans = 0
for i in product('12345678', repeat=9):
    i = ''.join(i)
    u1 = all([int(i[k]) % 2 != int(i[k+1]) % 2 for k in range(len(i) - 1)])
    u2 = all(i.count(k) <= 3 for k in i)
    if u1 and u2:
        ans += 1
print(ans)
