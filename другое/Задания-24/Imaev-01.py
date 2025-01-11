with open('imaev/24_1.txt') as file:
    st = file.readline()

st = st.replace('D', ' ').replace('E', ' ')

print(len(max(st.split(), key=len)))


