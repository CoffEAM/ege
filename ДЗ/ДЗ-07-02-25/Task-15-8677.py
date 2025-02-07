from itertools import combinations

def delet(x, y):
    return 1 if x%y==0 else 0

def f(x):
    b = 80 <= x <= 100
    a = a_a
    return delet(x, 17) <= ((not b) or (a < x + 30))

ans = []
line = [x/10 for x in range(79*10, 101*10)]
for a_a in range(1000):
    if all(f(x) for x in line):
        ans.append(a_a)
print(max(ans))



