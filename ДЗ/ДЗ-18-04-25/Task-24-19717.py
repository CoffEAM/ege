with open('txt/24.5_19717.txt') as file:
    st = file.readline()

st = st.split('M')
ans = 0
for i in range(len(st) - 278):
    ans = max(ans, len('M'.join(st[i:i+279])))

print(ans)
