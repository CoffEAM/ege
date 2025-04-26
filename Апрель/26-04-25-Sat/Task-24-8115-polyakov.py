from re import *

with open('txt/24-337.txt') as file:
    st = file.readline()

pattern = r'1[0-9A-D]+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
ans = 0
for i in res:
    for j in range(len(i) - 1):
        if i[j] != '1':
            continue
        for k in range(j + 1, len(i)):
            if int(i[j:k + 1], 14) % 7 == 0:
                ans = max(ans, len(i[j:k + 1]))
print(ans)
