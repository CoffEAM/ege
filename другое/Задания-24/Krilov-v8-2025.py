with open('txt-Krilov-2025/24var08.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')

ans = 0
for i in range(len(st)-701):
    if 'E' not in st[i:i+701]:
        ans = max(ans, len(''.join(st[i:i+701])) + 700)
print(ans)
