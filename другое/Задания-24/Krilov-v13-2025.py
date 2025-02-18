with open('txt-Krilov-2025/24var13-16.txt') as file:
    st = file.readline()

st = st.replace('00', '0 0')
st = st.split()
print(len(max(st, key=len)))
