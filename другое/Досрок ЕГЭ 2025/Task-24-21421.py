from re import finditer

with open('txt/24_21421.txt') as file:
    st = file.readline()

pattern = r'[1-9AB][0-9AB]*[02468A]'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len)))
