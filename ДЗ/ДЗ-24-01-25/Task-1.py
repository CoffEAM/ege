from itertools import permutations

graph = 'AG AE GC EC GF ED FB DB BC'.split()
matrix = '47 57 45 136 236 457 126'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

