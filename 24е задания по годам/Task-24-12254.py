from re import finditer

with open('txt/24_12254.txt') as file:
    st = file.readline()
#
# st = st.replace('RSQ', '*')
#
# for i in range(len(st)):
#     if st[i:i+17] == 17*'*':
#         print(st[i-3:i+20])
#
# print(17*3+3)

pattern = r'(SQ|Q)?(RSQ)+(RS|R)?'
print(max([len(i.group()) for i in finditer(pattern, st)]))
