with open('txt/24_17535.txt') as file:
    st = file.readline()

st = st.replace('CD', 'C*D')
st = st.split('*')
ans = 0
for i in range(len(st) - 160):
    ans = max(ans, len(''.join(st[i:i+161])))
print(ans)
