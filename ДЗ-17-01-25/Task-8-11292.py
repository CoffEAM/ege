from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

count = 0
for val in product(alph[:16], repeat=5):
    val = ''.join(val)
    if val.count('6') == 2:
        flag = False
        for i in product('2468ACE', repeat=3):
            i = ''.join(i)
            if i[1] == '6' and i not in val:
                flag = True
        if flag:
            count += 1
print(count)
