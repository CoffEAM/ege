from re import finditer

with open('txt/24_16388.txt') as file:
    st = file.readline()

pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
print(max([len(i.group()) for i in finditer(pattern, st)]))
