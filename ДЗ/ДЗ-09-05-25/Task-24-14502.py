from itertools import permutations
from string import ascii_uppercase
from re import finditer

with open('txt/24_14502.txt') as file:
    st = file.readline()

res = 1
seet = set()
for b1 in st:
    for b2 in st:
        res += 1
        seet.add(b2)
        if len(seet) == 26:
            print(res)
            exit()
