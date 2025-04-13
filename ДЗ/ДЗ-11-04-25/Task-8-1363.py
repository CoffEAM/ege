from itertools import product

ans = 0
for num in product('01234', repeat=6):
    num = ''.join(num)
    if num[0] == '3' and int(num, 5) % 2 == 0:
        ans += 1
print(ans)
