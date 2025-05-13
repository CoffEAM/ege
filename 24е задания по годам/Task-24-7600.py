from itertools import product

with open('txt/24_7600.txt') as file:
    st = file.readline()

st = st.replace('R', '*').replace('S', '*').replace('Q', '*')
st = st.replace('**', '* *')
st = st.split()
print(len(max(st, key=len)))
