from re import finditer

with open('txt/24_4627.txt') as file:
    st = file.readline()

pattern = r'(PNO|NPO)+(?=PNO|NPO)(PNO|NPO)'

matches = finditer(pattern, st)
matches = [i.group() for i in matches]
print(len(max(matches, key=len)))
