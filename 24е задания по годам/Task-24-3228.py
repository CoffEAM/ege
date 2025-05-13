with open('txt/24_3228.txt') as file:
    st = file.readline()

st = st.replace('AB', '*').replace('AC', '*')
for i in 'ABC':
    st = st.replace(i, ' ')
st = st.split()
print(len(max(st, key=len)))
