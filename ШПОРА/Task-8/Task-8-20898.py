from itertools import product
cnt = 0
for i in product('012345678', repeat=5):
    i = ''.join(i)
    if i[0] != '0' and i.count('0') == 1:
        for k in '1357':
            i = i.replace(k, '*')
        if '*0' not in i and '0*' not in i:
            cnt += 1
print(cnt)
