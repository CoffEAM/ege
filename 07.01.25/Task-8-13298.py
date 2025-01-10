from itertools import product

arr = []
for pos, val in enumerate(product(sorted('ПРИВЫЧКА'), repeat=5), start=1):
    arr.append([pos, ''.join(val)])
for i in arr:
    if i[0]%5==0:
        arr.remove(i)
for pos, val in enumerate(arr, start=1):
    if len(set(val[1])) == len(val[1]):
        if 'И' not in val[1] and 'Ы' not in val[1] and 'А' not in val[1]:
            print(pos)
            break


