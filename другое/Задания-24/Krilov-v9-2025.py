with open('txt-Krilov-2025/24var09.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')

ans = 0
for i in range(len(st)-4):
    ans = max(ans, len(''.join(st[i:i+4])) + 3)
print(ans)
