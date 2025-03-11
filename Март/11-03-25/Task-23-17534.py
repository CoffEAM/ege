def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    return f(x - 1, y) + f(x//2, y)

print(f(30,8)*f(8,  1))
