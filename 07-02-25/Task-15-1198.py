from binascii import a2b_qp
from itertools import combinations

def f(x):
    b = 18 <= x <= 52
    c = 16 <= x <= 41
    a = a1<=x<=a2
    return (b <= a) and ((not c) or a)

ans = []
line=[x/10 for x in range(15*10, 53*10)]
for a1,a2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(a2-a1)
print(min(ans))

