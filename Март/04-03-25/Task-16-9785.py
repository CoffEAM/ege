from sys import setrecursionlimit
setrecursionlimit(5000)
def f(n):
    if n < 7:
        return 7
    else:
        return n + 1 + f(n-2)

print(f(2024) - f(2020))
