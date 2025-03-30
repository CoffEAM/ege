with open('txt/24_4643.txt') as file:
    st = file.readline()

while '12A' in st or '21A' in st or '12B' in st or '21B' in st:
    st = st.replace('12A', '*').replace('21A', '*')
    st = st.replace('12B', '*').replace('21B', '*')

while '22A' in st or '22B' in st or '11B' in st or '11A' in st:
    st = st.replace('22A', '*').replace('11A', '*')
    st = st.replace('22B', '*').replace('11B', '*')

for i in '12AB':
    while i in st:
        st = st.replace(i, ' ')

st = st.split()

print(len(max(st, key=len)))
