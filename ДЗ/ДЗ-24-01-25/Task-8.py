from itertools import product
alph = '0123456789AB'
chet = '02468A'
nech = '13579B'

def con(num):
    res = ''
    while num:
        res += alph[num%12]
        num //= 12
    return res[::-1]


cnt = 0
for i in range(1000000, 10000000):
    r = con(i)
    if r.count('B')==2:
        flag = True
        for val in product(alph, repeat=2):
            val = ''.join(val)
            if val[0] in chet and val[1] in chet or val[0] in nech and val[1] in nech:
                if val in r:
                    flag = False
        if flag:
            cnt += 1

print(cnt)


