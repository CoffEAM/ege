from itertools import permutations

graph = 'AG AD GF GB AB DE DC BC FE'.split()
matrix = '26 147 456 236 37 134 25'.split()
print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
