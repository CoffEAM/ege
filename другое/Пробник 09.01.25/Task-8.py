from itertools import product
from string import ascii_uppercase,digits

alph = digits+ascii_uppercase
alph = alph[10:16] #ABCDEF
cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    if i[0]!='A' and i[0]!='E' and i[-1]!='A' and i[-1]!='E':
        cnt += 1
print(cnt)




