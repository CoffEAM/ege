from itertools import product

ans = 0
for val in product('01', repeat=20):
    val = ''.join(val)
    if val.count('0') == 19:
        ans += 1
print(ans)
