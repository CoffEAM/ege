from itertools import permutations

graph = 'AG GH HD DF FC CA AB CB EB ED'.split()
matrix = '56 378 26 68 17 134 258 247'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
