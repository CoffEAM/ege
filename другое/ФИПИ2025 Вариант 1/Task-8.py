from itertools import product

alph = '012345'

cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    if i[0]!='0' and i.count('0')==1:
        if '202' not in i and '204' not in i and '402' not in i and '404' not in i:
            cnt += 1
print(cnt)

#Otvet 13625


