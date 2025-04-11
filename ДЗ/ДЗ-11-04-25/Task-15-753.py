from binascii import a2b_qp
from itertools import combinations

def f(x):
    p = 5 <= x <= 30
    q = 14 <= x <= 23
    a = a1 <= x <= a2
    return (x == q) <= (not a)

ans = []
line = [i + eps for i in range(4, 31) for eps in [0, 0.1, 0.9]]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(max(ans))
