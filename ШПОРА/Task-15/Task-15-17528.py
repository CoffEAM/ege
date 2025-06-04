from itertools import combinations

def f(x):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2
    return p <= ((q and (not a)) <= (not p))

ans = []
line = [i + eps for i in range(14, 64) for eps in [0, 0.1, 0.9]]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))
