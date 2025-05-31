from itertools import permutations, product

def f1(x, y, z, w):
    return (w == x) and (y <= z)

def f2(x, y, z, w):
    return (w <= x) <= (y == z)

for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [
        (1, a1, 1, 1),
        (a2, 1, 0, 0),
        (a3, 0, 0, a4)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u1 = [f1(**dict(zip(p, t))) for t in table] == [1, 1, 0]
            u2 = [f2(**dict(zip(p, t))) for t in table] == [0, a5, 0]
            if u1 and u2:
                print(*p)
