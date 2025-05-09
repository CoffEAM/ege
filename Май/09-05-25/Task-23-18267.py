def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    if x != 6:
        return f(x + 2, y) + f(x + 5, y) + f(x ** 2, y)
    else:
        return f(x + 2, y) + f(x + 5, y)

print(f(4, 36))
