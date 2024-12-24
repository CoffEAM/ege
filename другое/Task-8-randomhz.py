from itertools import product
from string import ascii_uppercase
alph = ascii_uppercase

for i in range(1, 7):
    for pos, val in enumerate(product(alph, repeat=i), start=1):
        val = ''.join(val)
        if val=='FEDABC':
            print(pos)
            break


