from sys import setrecursionlimit
setrecursionlimit(4000)

def f(n):
    if n > 3000:
        return n
    else:
        return (2*n + 4) * f(n + 2)

res = int(f(20)/f(28))
summ = 0
for i in str(res):
    summ += int(i)
print(summ, res)


