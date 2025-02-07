from itertools import permutations

pars = ['ОО', 'ОА', 'АО']

cnt = 0
for val in set(permutations('СОТОЧКА')):
    val = ''.join(val)
    if any(par in val for par in pars):
        cnt += 1
print(cnt)


