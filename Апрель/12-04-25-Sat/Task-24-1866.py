from re import findall

with open('txt/24_1866.txt') as file:
    st = file.readline()

pattern = r'(?<=ad|da)\w+?(?=ad|da)'

match = findall(pattern, st)
print(len(max(match, key=len)))
