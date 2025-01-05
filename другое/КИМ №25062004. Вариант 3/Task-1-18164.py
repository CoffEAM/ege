from itertools import permutations

graph = 'AF AB FG BG FE BC GE GD ED CD'.split()
matrix = '3567 37 126 57 146 135 124'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

