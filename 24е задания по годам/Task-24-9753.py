with open('txt/24_9753.txt') as file:
    st = file.readline()

st = st.split('Y')
ans = 0
for i in range(len(st) - 150):
    ans = max(ans, len('Y'.join(st[i:i+151])))
print(ans)
