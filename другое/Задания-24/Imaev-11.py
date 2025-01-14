with open('imaev/24_22osn_PNO.txt') as file:
    st = file.readline()

st = st.replace('PNO', '#').replace('NPO', '#')
for i in 'NOP':
    st = st.replace(i, ' ')
st = st.split()
print(len(max(st, key=len)))

#327 - правильно

