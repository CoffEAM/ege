from itertools import product

ans = 0
for i in product(sorted('ГЕПАРД'), repeat=5):
    i = ''.join(i)
    if i[0] != 'А' and i[-1] != 'Е' and i.count('Г') == 1:
        ans += 1
print(ans)
