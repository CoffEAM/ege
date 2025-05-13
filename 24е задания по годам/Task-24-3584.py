with open('txt/24_3584.txt') as file:
    st = file.readline()

while 'DA' in st or 'BA' in st:
    st = st.replace('DA', '*').replace('BA', '*')
for i in 'ABD':
    st = st.replace(i, ' ')
st = st.split()
print(len(max(st, key=len)))
