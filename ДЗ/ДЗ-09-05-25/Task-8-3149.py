from itertools import product

u = [i*3 for i in '0123456789']

ans = 0
for num in product('0123456789', repeat=5):
    num = ''.join(num)
    if num[0] != '0' and num[-1] not in '347':
        fg = [i not in num for i in u]
        if all(fg):
            ans += 1
print(ans)
