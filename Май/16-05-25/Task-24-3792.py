with open('txt/24_3792.txt') as file:
    st = file.readline()

st = st.replace('D', ' ').replace('E', ' ').split()
print(len(max(st, key=len)))
