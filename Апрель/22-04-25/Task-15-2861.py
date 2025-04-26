from itertools import combinations

def f(x):
    p = 69 <= x <= 91
    q = 77 <= x <= 114
    a = a1 <= x <= a2
    return q <= ((p == q) or ((not p) <= a))

ans = []
line = [i + eps for i in range(68, 115) for eps in [0, 0.1, 0.9]]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))
