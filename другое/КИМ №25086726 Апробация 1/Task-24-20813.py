from re import finditer

with open('txt/24_20813.txt') as file:
    st = file.readline()

pattern = r'([7-9][0789]*[-*])+[7-9][0789]*'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(max(res, key=len))

pattern = r'[7-9][0789]*([-*][7-9][0789]*)+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(max(res, key=len))
