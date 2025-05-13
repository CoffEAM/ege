from re import finditer

with open('txt/24_2942.txt') as file:
    st = file.readline()

pattern = r'(AB|AC)+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(len(max(res, key=len))//2)
