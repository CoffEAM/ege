from sys import setrecursionlimit
setrecursionlimit(5000)
def f(n):
    if n < 110:
        return n
    else:
        return n + f(n-1)

print(f(2025) - f(2021))
