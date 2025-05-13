from re import finditer

with open('txt/24_6636.txt') as file:
    st = file.readline()

pattern = r'([24][135])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))//2)
