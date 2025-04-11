from itertools import product

ans = 0
for num in product('01234', repeat=6):
    num = ''.join(num)
    if num[0] == '3' and num[-1] in '024':
        ans += 1
print(ans)
