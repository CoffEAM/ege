'''Способ 1'''
from itertools import permutations, product

def f(x, y, w, z):
    return (w == (z <= x)) and y

for a1,a2,a3,a4,a5 in product([0, 1], repeat=5):
    table = [
        (a1,0,a2,0),
        (1,a3,1,1),
        (a4,a5,0,0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 0, 1]
            if u:
                print(*p)

'''Способ 2'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w == (z <= x)) and y:
                    print(x, y, z, w)
#ywzx
