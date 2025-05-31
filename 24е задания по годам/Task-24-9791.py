from re import finditer

with open('txt/24_9791.txt') as file:
    st = file.readline()

pattern = r'[1-9A-F]([1-9A-F])+'
res = [i.group() for i in finditer(pattern, st)]
ans = 0
for i in res:
    if int(i, 16) % 6 == 0:
        ans = max(ans, len(i))
    else:
        for c1 in range(len(i)):
            for c2 in range(len(i), c1, -1):
                if int(i, 16) % 6 == 0:
                    ans = max(ans, len(i[c1:c2]))
print(ans)
