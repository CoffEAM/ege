with open('txt/24_13715.txt') as file:
    st = file.readline()

st = st.replace('AB', 'A*B')
st = st.split('*')
ans = 0
for i in range(len(st) - 50):
    ans = max(ans, len(''.join(st[i:i+51])))
print(ans)

