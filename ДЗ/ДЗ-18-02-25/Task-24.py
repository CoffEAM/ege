with open('txt/24.txt') as file:
    st = file.readline()

st = st.replace('RSQ', '*')
for i in range(100, 0, -1):
    if '*'*i in st:
        print(st[st.find('*'*i)-3:st.find('*'*i)+i+3])
        break

ans = 'RS*****************SQ'

print(ans.count('*')*3)
