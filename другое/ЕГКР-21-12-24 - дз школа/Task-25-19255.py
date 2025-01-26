#54?1?3*7
from itertools import product

st = '54?1?3*7'
ans = []
for i in '0123456789':
    st = '54' + i + '1?3*7'
    for j in '0123456789':
        st = st[:4] + j + '3*7'
        for k in range(0, 4):
            for val in product('0123456789', repeat=k):
                st = st[:6] + ''.join(val) + '7'
                if int(st)%18579==0:
                    print(st, int(st)//18579)
                    ans.append(int(st))
print(sorted(ans))

