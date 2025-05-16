from re import finditer

with open('txt/24_6054.txt') as file:
    st = file.readline()

pattern = r'([BC][BC]A)+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len)))
