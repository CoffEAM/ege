from itertools import product

st = open('txt/24_8510.txt').readline()

for val in product('NOP', repeat=2):
    val = ''.join(val)
    st = st.replace(val, f'{val[0]}*{val[1]}')
st = st.split('*')
print(len(max(st, key=len)))

