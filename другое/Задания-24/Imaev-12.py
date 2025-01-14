with open('imaev/24-s1.txt') as file:
    st = file.readlines()

from string import ascii_uppercase

alph = ascii_uppercase

st = [i[:-1] for i in st]

cnt = 0
for i in st:
    if i.count('C')>i.count('B'):
        cnt += 1
print(cnt)

#491 - правильно
