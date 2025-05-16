with open('txt/24_7624.txt') as file:
    st = file.readline()

for i in 'XYZ':
    st = st.replace(i, '*')
st = st.replace('**', '* *')
st = st.split()
print(len(max(st, key=len)))
