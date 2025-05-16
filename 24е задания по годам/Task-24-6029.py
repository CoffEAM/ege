with open('txt/24_6029.txt') as file:
    st = file.readline()

while 'FF' in st or 'EE' in st:
    st = st.replace('FF', 'F F').replace('EE', 'E E')
st = st.replace('D', ' ')
st = st.split()
print(len(max(st, key=len)))
