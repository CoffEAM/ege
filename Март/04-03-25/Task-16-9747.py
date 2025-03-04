from sys import setrecursionlimit
setrecursionlimit(4000)
def f(n):
    if n < 11:
        return n
    else:
        return n + f(n-1)

print(f(2024) - f(2021))
