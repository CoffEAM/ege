from itertools import combinations

def f(x):
    P = 43 <= x <= 49
    Q = 44 <= x <= 53
    A = A1 <= x <= A2
    return (A<=P) or Q

ans = []
line = [x for x in range(40, 55)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2-A1)
print(max(ans))


