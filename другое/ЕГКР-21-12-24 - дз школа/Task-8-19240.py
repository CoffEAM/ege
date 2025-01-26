from itertools import product

arr = []
for pos, val in enumerate(product(sorted('ЯНВАРЬ'), repeat=5), start=1):
    val = ''.join(val)
    if val[0]!='Я' and val.count('Ь')<=1 and 'ЯЯ' not in val:
        arr.append([pos, val])
print(max(arr))


