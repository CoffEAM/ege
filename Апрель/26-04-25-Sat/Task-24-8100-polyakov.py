from re import *

with open('txt/24-335.txt') as file:
    st = file.readline()

p1 = r'([1-9][0-9]*[^05+)(-])'
p2 = r'([1-9][0-9]*[05])'
pattern = fr'(\({p1}[+-]{p2}\))+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(len(max(res, key=len)))
