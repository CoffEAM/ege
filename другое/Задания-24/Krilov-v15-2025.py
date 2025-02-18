with open('txt-Krilov-2025/24var13-16.txt') as file:
    st = file.readline()

st = st.replace('12', '1 2').replace('21', '2 1')
st = st.split()
print(len(max(st, key=len)))
