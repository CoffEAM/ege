from itertools import product, permutations

alph = '012345'

cnt = 0
for i in product(alph, repeat=6):
    i = ''.join(i)
    if i[0]!='0' and i.count('0')==1:
        flag = False
        for val in permutations('0135', 3):
            val = ''.join(val)
            if val[1] == '0':
                if val not in i:
                    flag = True
        if flag:
            cnt += 1
print(cnt)

#Otvet 13625


