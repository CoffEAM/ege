from itertools import permutations

graph = 'АБ АВ АГ БД ГВ ГЖ ГЕ ГЗ ВЖ ВД ЖД ДЕ ЗЕ'.split()
matrix = '457 37 267 1678 16 3458 12348 467'.split()
print(*range(1, 9))
for i in permutations('АБВГДЖЗЕ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
