from itertools import permutations

graph = 'АБ АВ БВ БД ВЕ ДЕ ДГ ДЖ ЕЖ ЕЗ ЗЖ ГЖ'.split()
matrix = '3578 346 1258 26 13 248 18 1367'.split()
print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
