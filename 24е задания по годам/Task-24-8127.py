from re import finditer

with open('txt/24-347.txt') as file:
    st = file.readline()

ans = []
leen = 0
pattern = r'[1-7][0-7]*'
res = [i.group() for i in finditer(pattern, st)]
for i in res:
    if int(i, 8) % 13 == 0:
        ans.append(i)
arr = []
for i in ans:
    if len(i) == 16:
        arr.append(i)
print(st.index('1236504706541237'))
