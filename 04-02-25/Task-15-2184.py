from binascii import a2b_qp
from itertools import combinations

def f(x):
    p = 1<=x<=39
    q = 23<=x<=58
    a = a1 <= x<= a2
    return (p <= (not q)) <= (not a)

ans = []
line = [x/10 for x in range(0, 59*10)]

for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(max(ans))


