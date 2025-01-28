from itertools import product
st = open('txt/24_17685.txt').readline()
for i in ['**', '*+', '+*', '++']:
    st = st.replace(i, ' ')

while ' 0 ' in st:
    st = st.replace(' 0 ', ' ')

while f'+ ' in st or f'* ' in st:
    st = st.replace(f'+ ', f' ')
    st = st.replace(f'* ', f' ')
while f' +' in st or f' *' in st:
    st = st.replace(f' +', f' ')
    st = st.replace(f' *', f' ')

print(len(max([i for i in st.split() if eval(i)==0], key=len)))

