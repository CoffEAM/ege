with open('txt-Krilov-2025/24var12.txt') as file:
    st = file.readline()

st = st.replace('AB', 'A*B')
st = st.split('*')
ans = 0
for i in range(len(st)-22):
    ans = max(ans, len(''.join(st[i:i+22])))
print(ans)
