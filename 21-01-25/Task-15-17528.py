P = [i for i in range(15, 41)]
Q = [i for i in range(21, 64)]
def f(A):
    for x in range(1000):
        f = (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))
        if not f:
            return 0
    return 1

for i in range(100):
    for k in range(100):
        A = [l for l in range(i, k)]
        if f(A):
            print(A)
            break


