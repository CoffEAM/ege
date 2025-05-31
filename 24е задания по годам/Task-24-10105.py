with open('txt/24_10105.txt') as file:
    st = file.readline()

st = st.split('T')
ans = 0
for i in range(len(st) - 100):
    ans = max(ans, len('T'.join(st[i:i+101])))
print(ans)
