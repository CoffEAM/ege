with open('imaev/AUBCD.txt') as file:
    st = file.readline()

#ABCDU
st = st.replace('A', '*').replace('U', '*')
st = st.replace('B', '-').replace('C', '-').replace('D', '-')
st = st.replace('-*', '#')
for i in 'ABCDU-*':
    st = st.replace(i, ' ')
print(len(max(st.split(), key=len)))

#174 правильно

