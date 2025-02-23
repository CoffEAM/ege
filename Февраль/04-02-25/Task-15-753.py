from itertools import combinations

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = A1 <= x <= A2
    return (P == Q) <= (not A)

ans = []
line = [x / 10 for x in range(2 * 10, 35 * 10)]

for A1, A2 in combinations(line, 2):
    if all(f(x) for x in line):
        ans.append(A2-A1)
print(max(ans))

