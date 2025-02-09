from itertools import permutations

graph = 'BA BG GE AC AD CF FD CE EF'.split()
matrix = '247 145 456 123 23 37 16'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
#29
