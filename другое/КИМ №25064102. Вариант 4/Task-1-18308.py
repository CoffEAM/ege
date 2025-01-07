from itertools import permutations

graph = 'AK BK KC BD CD DE DG DH EF HG FG'.split()
matrix = '45 489 45 12379 136 5 48 27 24'.split()

print(*range(1, 10))
for i in permutations('ABCDEFGHK'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


