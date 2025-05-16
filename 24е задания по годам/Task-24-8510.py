with open('txt/24_8510.txt') as file:
    st = file.readline()

for i in 'NOP':
    st = st.replace(i, '*')
while '**' in st:
    st = st.replace('**', '* *')
st = st.split()
print(len(max(st, key=len)))
