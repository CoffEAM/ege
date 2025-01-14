# Способ 1
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ( (not(w<=z)) or (x<=y) or (not x) ) == 0:
#                     print(x, y, z, w)
#
# Способ dva
from itertools import product, permutations


def f(x, y, z, w):
    return (not (w <= z)) or (x <= y) or (not x)


for a1, a2, a3, a4, a5, a6, a7 in product([1, 0], repeat=7):
    table = [
        (1, a1, a2, a3),
        (0, 1, 0, a4),
        (a5, 0, a6, a7)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)
