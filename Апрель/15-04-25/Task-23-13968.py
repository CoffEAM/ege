def f(x, y):
    if x == y: return 1
    if x > y or x == 21: return False
    return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)


print(f(7, 14) * f(14, 32))
