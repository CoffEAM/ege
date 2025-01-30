from string import digits, ascii_uppercase
from itertools import product
alph = digits + ascii_uppercase
alph = alph[:12]
chet = ''.join([i for i in alph if (alph.index(i)+1)%2==0])
nechet = ''.join([i for i in alph if (int(i, 12)+1)%2==0])

def con(num):
    res = ''
    while num:
        res += alph[num%12]
        num //= 12
    return res[::-1]

cnt = 0
for num in product('0123456789', repeat=7):
    num = ''.join(num)
    if num[0] != '0':
        num = con(int(num))
        if num.count('B')==2:
            flag = False
            for r in range(len(num)-1):
                if (int(num[r], 12)%2==0 and int(num[r+1], 12)%2==1) or (int(num[r], 12)%2==1 and int(num[r+1], 12)%2==0):
                    flag = True
                else:
                    flag = False
            if flag:
                cnt += 1
print(cnt)




