from itertools import product

ans = 0
for num in product('012345678', repeat=7):
    num = ''.join(num)
    if num[0] in '2468' and num.count('6') >= 1:
        if num[-1] in '124578':
            ans += 1
print(ans)
