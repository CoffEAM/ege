from itertools import product
st = open('txt/24_17685.txt').readline()
for i in ['**', '*+', '+*', '++']:
    st = st.replace(i, ' ')

while ' 0 ' in st:
    st = st.replace(' 0 ', ' ')

for i in '0123456789':
    while f'{i}+ ' in st or f'{i}* ' in st:
        st = st.replace(f'{i}+ ', f'{i} ')
        st = st.replace(f'{i}* ', f'{i} ')
    while f' +{i}' in st or f' *{i}' in st:
        st = st.replace(f' +{i}', f' {i}')
        st = st.replace(f' *{i}', f' {i}')

print(len(max([i for i in st.split() if eval(i)==0], key=len)))

