from itertools import product

ans = 0
for num in product('01234567', repeat=5):
    num = ''.join(num)
    if num[0] != '0' and num.count('6') == 1:
        for i in '1357':
            num = num.replace(i, '*')
        if '6*' not in num and '*6' not in num:
            ans += 1
print(ans)
