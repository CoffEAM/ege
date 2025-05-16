from re import finditer

with open('txt/24_4627.txt') as file:
    st = file.readline()

pattern = r'(NPO|PNO)+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(len(max(res, key=len))//3)
