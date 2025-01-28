from string import digits, ascii_uppercase
from itertools import product

alph = digits+ascii_uppercase
alph = alph[:25]

cnt = 0
for num in product(alph, repeat=4):
    num = ''.join(num)
    cnt_nechet = 0
    cnt_bolsh = 0
    if num[0] != '0':
        for i in num:
            if int(i, 25)%2==1:
                cnt_nechet += 1
            if int(i, 25) <= 5:
                cnt_bolsh += 1
        if cnt_nechet == 1 and cnt_bolsh <= 2:
            cnt += 1
print(cnt)


