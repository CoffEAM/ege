with open('imaev/24_1.txt') as file:
    st = file.readline()

st = st.replace('AA', 'A A').replace('BB', 'B B')
st = st.replace('CC', 'C C').replace('DD', 'D D')
st = st.replace('EE', 'E E')
st = st.replace('AA', 'A A').replace('BB', 'B B')
st = st.replace('CC', 'C C').replace('DD', 'D D')
st = st.replace('EE', 'E E')

print(len(max(st.split(), key=len)))


