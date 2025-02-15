with open('txt-Krilov-2025/24var11.txt') as file:
    st = file.readline()

st = st.replace('AB', '*')
st = st.split('*')
ans = 99999999
for i in range(len(st)-21):
    ans = min(ans, len(''.join(st[i+1:i+21]))+42)
print(ans)
