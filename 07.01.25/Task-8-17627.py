from itertools import product
from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

ans = 0
for val in product(alph[:15], repeat=5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0]!='0':
        cnt = 0
        for i in 'ABCDE':
            cnt += val.count(i)
        if cnt>=2:
           ans += 1
print(ans)



