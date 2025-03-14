def f(x, y, b=False):
    if x == y: return 1
    elif x > y: return 0
    if b:
        return f(x + 2, y) + f(x * 3, y)
    return f(x + 2, y) + f(x**2, y, True) + f(x * 3, y)

print(f(2, 64))
