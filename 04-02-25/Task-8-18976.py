from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase
alph = alph[:20]
chet = [i for i in alph if int(i, 20)%2==0]
nechet = [i for i in alph if int(i, 20)%2==1]

ans = 0
for num in product(alph, repeat=5):
    num = ''.join(num)
    k = ''.join(num)
    for i in num:
        if i in chet:
            num = num.replace(i, '+')
        elif i in nechet:
            num = num.replace(i, '-')
    if '--' not in num and '++' not in num:
        if int(k[0], 20) + int(k[-1], 20) == 26 and k[0]!='0':
            ans += 1
print(ans)





