from re import *

with open('txt/24-314.txt') as file:
    st = file.readline()

num = r'([1-7][0-7]*)|0'
pattern = fr'(?<=F){num}([+*]{num})+'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(eval(max(res, key=len)))


