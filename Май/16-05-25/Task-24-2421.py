with open('txt/24_2421.txt') as file:
    st = file.readline()

st = st.replace('D', ' ').split()
print(len(max(st, key=len)))
