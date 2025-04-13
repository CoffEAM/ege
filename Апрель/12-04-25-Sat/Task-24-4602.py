from re import findall, finditer

with open('txt/24_4602.txt') as file:
    st = file.readline()

pattern = r'([BCD][AO])+'

matches = finditer(pattern, st)
matches = [i.group() for i in matches]
print(len(max(matches, key=len)))
