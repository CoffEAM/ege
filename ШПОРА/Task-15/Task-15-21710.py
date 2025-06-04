from itertools import combinations

def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = a1 <= x <= a2
    return (not a) <= (b == c)

ans = []
line = [i + eps for i in range(25, 111) for eps in [0, 0.1, 0.9]]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))
