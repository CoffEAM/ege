from string import digits
from itertools import product

chet= '02468'
st = '1592#6?8'
for i in digits:
    st = f'1592#6{i}8'
    for n in range(1, 5):
        for j in product(chet, repeat=n):
            j = ''.join(j)
            st = f'1592{j}{st[-3:]}'
            if int(st)%1996==0:
                print(st, int(st)/1996)




