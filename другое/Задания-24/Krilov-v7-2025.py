with open('txt-Krilov-2025/24var07.txt') as file:
    st = file.readline()

st = st.replace('A', '*')
st = st.split('*')

ans = 9999999999
for i in range(len(st) - 500):
    ans = min(ans, len(''.join(st[i+1:i+500])) + 500)
print(ans)
