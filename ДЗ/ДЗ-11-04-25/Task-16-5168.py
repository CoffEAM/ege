from sys import setrecursionlimit

setrecursionlimit(6000)

def f(n):
    if n >= 10000: return n
    elif n % 2 == 0 and n < 10000: return f(n + 1) + n ** 2 - 3 * (n - 1)
    elif n % 2 == 1 and n < 10000: return f(n + 2) + 5 * n - (n - 1)

print(f(90) - f(99))
