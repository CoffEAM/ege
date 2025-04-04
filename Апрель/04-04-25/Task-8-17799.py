from itertools import product

for pos, val in enumerate(product(sorted('АРГУМЕНТ'), repeat=4), start=1):
    val = ''.join(val)
    if len(val) == len(set(val)) and sorted(val) == list(val):
        print(pos, val)
