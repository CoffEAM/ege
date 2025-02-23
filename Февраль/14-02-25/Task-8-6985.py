from itertools import product

for pos,val in enumerate(product(sorted('МАРКСЛ'), repeat=6), start=1):
    val = ''.join(val)
    if 'КС' not in val and 'СК' not in val:
        u = [val.count(i) for i in val]
        if u.count(3)==3 and u.count(1)==3:
            print(pos, val)

