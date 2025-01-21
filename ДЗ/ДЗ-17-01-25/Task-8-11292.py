from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase
count = 0
for val in product(alph[:16], repeat=5):
    val = ''.join(val)
    if val.count('6') == 2 and val[0]!='0':
        flag = False
        for i in product('02468ACE', repeat=2):
            i = ''.join(i)
            if i not in val and '6' in i:
                flag = True
        if flag:
            count += 1
print(count)
