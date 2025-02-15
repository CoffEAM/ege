from itertools import product
#10000000000

st = '12*567?'
for i in '0123456789':
    st = st[:-1] + i
    for k in range(4):
        for val in product('0123456789', repeat=k):
            val = ''.join(val)
            st = st[:2] + val + st[-4:]
            if int(st)%7777==0 and (1+int(st))%2==1:
                print(st, int(st)&7777)
