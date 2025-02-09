from sys import setrecursionlimit
setrecursionlimit(3100)

def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n + f(n-1)

print(f(3000) - f(2000))

#2500500
