with open('txt/24_1975.txt') as file:
    st = file.readline()

while 'PP' in st:
    st = st.replace('PP', 'P P')
st = st.split()
print(len(max(st, key=len)))
