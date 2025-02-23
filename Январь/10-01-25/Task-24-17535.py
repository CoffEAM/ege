with open('Txt-24-17535.txt') as file:
    st = file.readline()

st = st.replace('CD', '*')
for i in 'ABCDEF':
    st = st.replace(i, '1')

ans = []
for i in st:
    cnt = 0
    cnt_cd = 0
    for j in st[st.index(i):]:
        cnt += 1
        if j=='*':
            cnt_cd += 1
        if cnt_cd == 160:
               ans.append(cnt+160)
print(max(ans))



