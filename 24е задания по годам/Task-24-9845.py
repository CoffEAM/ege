from re import finditer

with open('txt/24_9845.txt') as file:
    st = file.readline()

pattern = r'([ABC][89])+|([89][ABC])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len)))
