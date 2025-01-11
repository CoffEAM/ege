from itertools import permutations

graph = 'CB CD BA DA DE BG GA GF FE'.split()
matrix = '234 156 17 15 246 257 36'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


