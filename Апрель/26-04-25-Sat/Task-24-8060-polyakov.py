from re import *

with open('txt/24-333.txt') as file:
    st = file.readline()

name = r'([0-9a-zA-Z][0-9a-zA-Z\.]+[0-9a-zA-Z])'
server = r'(yandex.ru|gmail.com)'
pattern = fr'{name}@{server}'
matches = finditer(pattern, st)
res = [i.group() for i in matches]
print(len(max(res, key=len)))

