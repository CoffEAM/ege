import sys

sys.setrecursionlimit(3000)

def f(n):
    if n>3000:
        return n
    elif n<=3000 and n%2==0:
        return n + f(n+1) + 1
    elif n<=3000 and n%2==1:
        return f(n+2) + 2

print(f(40)- f(43))


