def dele(n, m):
    if n%m == 0:
        return 1
    else:
        return 0

def f(A):
    for x in range(1, 1000):
        f = dele(A, x) <= (x == A)
        if not f:
            return 0
    return 1

cnt = 0
for a in range(1, 11111):
    if f(a):
        cnt += 1
print(cnt)



