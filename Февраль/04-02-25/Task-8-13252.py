from itertools import permutations

cnt = 0
for i in set(permutations('КИДАЛА', 5)):
    i = ''.join(i)
    if 'АА' not in i:
        cnt += 1
print(cnt)


