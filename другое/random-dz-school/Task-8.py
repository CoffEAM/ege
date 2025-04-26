from itertools import product
from string import digits, ascii_uppercase
alph = digits + ascii_uppercase

def c(num):
    res = ''
    while num:
        res += alph[num % 12]
        num //= 12
    return res[::-1]

ans = 0
for num in product('0123456789', repeat=6):
    num = ''.join(num)
    if num[0] != '0':
        u = c(int(num))[0]
        if int(num) % int(u, 12) == 0:
            ans += 1
print(ans)
