from binascii import a2b_qp
from itertools import combinations

def f(x):
    p = 13 <= x<= 19
    q = 17 <= x <= 23
    a = a1 <= x <= a2
    return (not((not p ) <= q)) <= (a <= ((not q) <= p))

ans = []
line = [x/10 for x in range(12*10, 24*10)]
for a1, a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(max(ans))


