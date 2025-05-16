from re import finditer

with open('txt/24_4602.txt') as file:
    st = file.readline()

pattern = r'([BCD][AO])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))//2)
