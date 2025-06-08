with open('txt/24_9845.txt') as file:
    st = file.readline()

for i in 'ABC':
    for j in 'ABC':
        st = st.replace(i+j, f'{i} {j}')
for i in '89':
    for j in '89':
        st = st.replace(i+j, f'{i} {j}')
st = st.split()
print(len(max(st, key=len)))
