with open('txt/24.5_19717.txt') as file:
    st = file.readline()

st = st.replace('M', ' ')
st = st.split()
ans = 0
for i in range(len(st) - 278):
    ans = max(ans, len(''.join(st[i:i+279])) + 278)

print(ans)
