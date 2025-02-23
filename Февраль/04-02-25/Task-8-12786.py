from itertools import permutations

cnt = 0
for i in set(permutations('МАКАКА', 6)):
    i = ''.join(i)
    if 'АА' not in i and 'КК' not in i:
        cnt += 1
print(cnt)


