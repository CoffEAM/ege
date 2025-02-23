from binascii import a2b_qp
from itertools import combinations

def f(x):
    p = 64<=x<=91
    q = 77<=x<=114
    a = a1<=x<=a2
    return q <= ((p == q) or ((not p )<= a))

ans = []
line = [x/10 for x in range(68*10, 115*10)]

for a1,a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))


