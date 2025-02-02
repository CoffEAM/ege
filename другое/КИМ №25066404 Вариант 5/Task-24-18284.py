from itertools import product

st = open('txt/24_18284.txt').readline()

love = ('L', 'O', 'V', 'E')

for i in 'REVOLUTION':
    if i not in 'LOVE':
        st = st.replace(i, '*')

for i in range(50, 0, -1):
    if i*'*' in st:
        st = st.replace(i*'*', f' {str(len(i*'*'))} ')

for i in range(50, 0, -1):
    for k in 'LOVE':
        if k*i in st:
            st = st.replace(k*i, f'{str(len(k*i))}-{k}')
st = st.replace('-1-', '-')
st = st.split()
arr = []
for i in st:
    if 'L' in i and i not in arr:
        arr.append(i)







