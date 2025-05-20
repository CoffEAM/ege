with open('txt/24_19489.txt') as file:
    st = file.readline()

st = st.replace('WWF', 'WW*WF').replace('WSFWW', 'WSFW+SFWW')
st = st.split('+')
ans = 0
for i in st:
    u = ''.join(st[i:i+121]).split('*')
    ans = max(ans, len(max(u, key=len)))
print(ans)
