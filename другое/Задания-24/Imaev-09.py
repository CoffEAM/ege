with open('imaev/24_22dosr.txt') as file:
    st = file.readline()

st = st.replace('AB', '*').replace('CB', '-')
st = st.replace('A', ' ').replace('B', ' ').replace('C', ' ')
print(len(max(st.split(), key=len)))


