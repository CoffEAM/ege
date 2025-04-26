from re import *

with open('txt/24-332.txt') as file:
    st = file.readline()

slovo = r'([A-C]?[a-c]+)'
pattern = fr'[A-C][a-c]*([ ]{slovo})+\.'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(len(max(res, key=len)))
