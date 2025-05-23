with open('txt/24_7662.txt') as file:
    st = file.readline()

st = st.replace('SOLO', '*')
st = st.split('*')
ans = 0
for i in range(len(st) - 4):
    l = 'SOLO'.join(st[i:i+5])
    cnt = sum(1 for i in '0123456789' if i in l)
    if cnt >= 5:
        ans = max(ans, len(l))
print(ans + 6)
