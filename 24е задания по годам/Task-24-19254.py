with open('txt/24_19254.txt') as file:
    st = file.readline()

st = st.split('FSRQ')
ans = 0
for i in range(len(st) - 80):
    ans = max(ans, len('FSRQ'.join(st[i:i+81])))
print(ans + 6)
