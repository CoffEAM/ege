from re import finditer

with open('txt/24_6757.txt') as file:
    st = file.readline()

pattern = r'(CFE|FCE)+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))/3)
