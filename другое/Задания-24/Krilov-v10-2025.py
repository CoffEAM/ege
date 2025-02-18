with open('txt-Krilov-2025/24var10.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')
ans = 99999999
for i in range(len(st)-35):
    ans = min(ans, len(''.join(st[i+1:i+35])) + 35)
print(ans)
