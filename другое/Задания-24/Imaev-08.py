with open('imaev/24_1.txt') as file:
    st = file.readline()

st = st.replace('ACCB', 'ACC CCB')
st = st.split()
print(len(max(st, key=len)))

#1336 - правильно


