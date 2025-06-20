from itertools import permutations

graph = 'AB BD DG GC CE EF FA FB ED'.split()
matrix = '256 134 267 27 16 135 34'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
