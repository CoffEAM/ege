from itertools import product

ans = 0
for num in product('0123456', repeat=5):
    num = ''.join(num)
    for i in '0246':
        num = num.replace(i, '*')
    cnt1 = num.count('***')
    cnt2 = num.count('**')
    if cnt1 == 0 and cnt2 >= 2:
        ans += 1
print(ans)
