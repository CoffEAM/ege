def f(x, y, a=False):
    if x == y: return 1
    elif x > y + 1: return 0
    if a:
        return f(x * 2, y) + f(x * 3, y)
    return f(x - 1, y, True) + f(x * 2, y) + f(x * 3, y)

print(f(3, 15))
