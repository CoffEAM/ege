with open('txt/24.txt') as file:
    st = file.readline()

st = st.replace('RSQ', '*')
for i in range(1000, 0, -1):
    if '*'*i in st:
        print(st[st.find('*'*i)-3:st.find('*'*i)+i+2])
        break

ans = '*****************SQ'

print(ans.count('*')*3 + 2)
