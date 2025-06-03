from itertools import product

for pos, val in enumerate(product(sorted('ПОБЕДА'), repeat=6)):
    val = ''.join(val)
    if val[0] == 'О' and len(val) == len(set(val)):
        print(pos, val)
