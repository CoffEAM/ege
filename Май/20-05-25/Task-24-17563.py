from re import finditer

with open('txt/24_17563.txt') as file:
    st = file.readline()

pattern = r'[7-9][0789]*([-*][7-9][0789]*)*'
res = [len(i.group()) for i in finditer(pattern, st)]
print(max(res))
