with open('txt/24_1866.txt') as file:
    st = file.readline()

while 'ad' in st or 'da' in st:
    st = st.replace('ad', 'a d').replace('da', 'd a')
st = st.split()
print(len(max(st, key=len)))
