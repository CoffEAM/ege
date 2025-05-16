from re import finditer

with open('txt/24_4682.txt') as file:
    st = file.readline()

pattern = r'([AE][BCD])+'
res = [i.group() for i in finditer(pattern, st)]
print(len(max(res, key=len))//2)
