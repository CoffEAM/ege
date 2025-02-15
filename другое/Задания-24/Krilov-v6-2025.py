with open('txt-Krilov-2025/24var06.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')

ans = 0
for i in range(len(st)-351):
    ans = max(ans, len(''.join(st[i:i+351])) + 350)
print(ans)
