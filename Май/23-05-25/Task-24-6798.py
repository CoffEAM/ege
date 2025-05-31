from re import finditer

with open('txt/24_6798.txt') as file:
    st = file.readline()

pattern = r'([CDF][ACDFO][AO])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len)))
