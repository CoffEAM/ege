import sys
sys.setrecursionlimit(3000)

def f(n):
    if n < 10:
        return n - 1
    elif n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    else:
        return 5 * n + 2 + f(n - 4)

print(f(4445) - f(4444))


