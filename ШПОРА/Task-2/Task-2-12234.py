from itertools import product, permutations

def f(x, y, z, w):
    return y and (x or z) or (not(y or z)) or w

for a1,a2,a3,a4 in product([0, 1], repeat=4):
    table = [
        (1,a1,0,1),
        (a2,1,0,a3),
        (0,0,a4,1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(''.join(p))
