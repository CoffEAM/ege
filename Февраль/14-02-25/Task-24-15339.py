from itertools import product

with open('txt/24_15339.txt') as file:
    st = file.readline()

# ABC  --  6789
for val in product('ABC', repeat=2):
    val = ''.join(val)
    while val in st:
        st = st.replace(val, f'{val[0]} {val[1]}')
for val in product('6789', repeat=2):
    val = ''.join(val)
    while val in st:
        st = st.replace(val, f'{val[0]} {val[1]}')
print(len(max(st.split(), key=len)))

