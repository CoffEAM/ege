from re import finditer

with open('txt/24_4643.txt') as file:
    st = file.readline()

pattern = r'([12][12][AB])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))/3)
