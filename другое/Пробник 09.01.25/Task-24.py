from string import ascii_uppercase
alph = ascii_uppercase
with open('txt/24_11636.txt') as file:
    st = file.readline()

for i in alph:
    if i != 'A':
        st = st.replace(i, '*')
st = st.replace('A', 'A A')
st = st.replace('AA', ' ')
st = st.split()
st = [1 for i in st if i.count('A')==2]
print(len(st))



