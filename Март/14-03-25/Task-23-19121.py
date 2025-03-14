def f(x, y):
    if x == y:
        return 1
    elif x <y:
        return 0
    return f(x - 3, y) + f(x // 3, y)

print(f(35, 8)*f(8, 1))
