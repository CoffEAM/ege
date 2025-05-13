from re import finditer

with open('txt/24_9791.txt') as file:
    st = file.readline()

pattern = r'[1-9A-F]([1-9A-F])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len)))
