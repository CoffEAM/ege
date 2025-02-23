from itertools import permutations

graph = 'AB AG AV VB VD BG GD DE DZ GJ EZ EJ JZ'.split()
matrix = '256 1458 478 237 126 158 348 2367'.split()
print(*range(1, 9))
for i in set(permutations('ABVGDEJZ')):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

