from re import finditer

with open('txt/24_15339.txt') as file:
    st = file.readline()

pattern = r'([ABC][6-9])+|([6-9][ABC])+'
print(max([len(i.group()) for i in finditer(pattern, st)]))
