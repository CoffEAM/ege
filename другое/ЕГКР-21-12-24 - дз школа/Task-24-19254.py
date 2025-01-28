st = open('txt/Txt-24-19254.txt').readline()

st = st.replace('FSRQ', ' ')
st = st.split()

ans = 0
for i in range(len(st)-81):
    ans = max(ans, len(''.join(st[i:i+81])))

print(ans)

