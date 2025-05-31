from re import finditer

with open('txt/24-335.txt') as file:
    st = file.readline()

pattern = r'(\(([1-9][0-9]*[12346789])[+-]([1-9][0-9]*[05])\))+'
res = [i.group() for i in finditer(pattern, st)]
print(max(res, key=len))
print(len(max(res, key=len)))
