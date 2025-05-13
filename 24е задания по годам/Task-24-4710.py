from re import finditer

with open('txt/24_4710.txt') as file:
    st = file.readline()

pattern = r'([CDF][AO])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))//2)
