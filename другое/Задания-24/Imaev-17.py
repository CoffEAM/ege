st = open('imaev/24_23dosr.txt').readline()
from itertools import product

for i in product('ABC', repeat=2):
    i = ''.join(i)
    st = st.replace(i, f'{i[0]} {i[1]}')

st = st.split()
print(len(max(st, key=len)))

#85 - правильно
