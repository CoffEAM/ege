import math
def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    else:
        return f(x-4, y) + f(x-7, y) + f(math.floor(x**0.5), y)


print(f(44, 22)*f(22, 3))


