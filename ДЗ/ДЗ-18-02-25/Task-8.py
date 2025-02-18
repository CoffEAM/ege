from itertools import product

alph = sorted(set('КАЛЕЙДОСКОП'))[::-1]
print(alph)

for pos, val in enumerate(product(alph, repeat=6), start=0):
    val = ''.join(val)
    if pos%2==0 and val[0]=='К' and val.count('Й')>=2 and val.count('С') == 0 and val.count('Е') == 0:
        print(pos, val)
