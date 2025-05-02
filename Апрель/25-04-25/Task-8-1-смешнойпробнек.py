from itertools import product

alph = '0123456789ABCD'
ans = 0
# u = sum(1 for i in num if i in 'ABCD') <= 4
for num in product(alph, repeat=6):
    num = ''.join(num)
    if num.count('0') == 0 and sum(1 for i in num if i in 'ABCD') <= 4:
        ans += 1
print(ans)
