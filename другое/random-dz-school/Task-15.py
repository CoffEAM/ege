from itertools import combinations

def f(x):
    p = x in [i for i in range(1, 7)]
    q = x in [3, 5, 15]
    a = a1 <= x <= a2
    return (not a) <= ((not p) and q) or (not q)

ans = []
line = [i + eps for i in range(100) for eps in [0, 0.1, 0.9]]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))
