from itertools import product

for pos, val in enumerate(product(sorted('ЛАЙМ'), repeat=5), start=1):
    val = ''.join(val)
    if val.count('М')==0 and val.count('Л')==0 and 'ЙЙ' not in val:
        print(pos, val)

