from itertools import permutations

graph = 'AB AC BC BD CE DE DF EG FG'.split()
matrix = '67 567 457 35 234 12 123'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

