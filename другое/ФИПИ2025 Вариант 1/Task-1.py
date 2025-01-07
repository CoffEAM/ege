from itertools import permutations

graph = 'AB AC BC BD CE DE DF EG FG AG'.split()
matrix = '237 167 156 567 34 234 124'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

#Ответ 24




