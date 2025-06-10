with open('txt/24_23206.txt') as file:
    st = file.readline()

for i in '02468':
    while i in st:
        st = st.replace(i, ' *')

st = st.split()
ans = 0
for i in st:
    if i.count('S') == 35:
        ans = max(ans, len(i))
    elif i.count('S') > 35:
        for k in range(len(i), 0, -1):
            sub_st = i[:k]
            if sub_st.count('S') == 35:
                ans = max(ans, len(sub_st))
                break
print(ans)
