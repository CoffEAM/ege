from string import digits
from itertools import product
from tabnanny import process_tokens

alph = digits
#1*28?64
#1000000(000000)
st = '1*28?64'
cnt = 0
summ = 0
for j in alph:
    st = st[:-3] + j + '64'
    for k in range(7):
        for l in product(alph, repeat=k):
            st = '1' + ''.join(l) + st[-5:]
            if int(st)%596==0:
                cnt += 1
                summ += int(st)
print(cnt, summ/cnt)





