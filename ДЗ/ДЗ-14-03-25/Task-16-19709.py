from sys import setrecursionlimit
setrecursionlimit(4000)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n**3 + f(n - 1)

print(f(2025) - f(2022))
