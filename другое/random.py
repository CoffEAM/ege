from itertools import permutations

def f(x, y, z):
    return (x <= (not z)) and ((not y) <= x)

table = [
    (0,1,0),
    (1,1,0)
]
for p in permutations('xyz'):
    u = [f(**dict(zip(p, t))) for t in table] == [0, 1]
    if u:
        print(*p)
