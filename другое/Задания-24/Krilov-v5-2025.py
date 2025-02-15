with open('txt-Krilov-2025/24var05.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')

ans = 12309412304
for i in range(len(st)-2024):
    ans = min(ans, len(''.join(st[i+1:i+2024]))+2024)

print(ans)
