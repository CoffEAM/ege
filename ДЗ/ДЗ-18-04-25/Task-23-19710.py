def f(x, y):
    if x == y: return 1
    elif x > y or x == 8: return 0
    return f(x + 3, y) + f(x * 2, y)

print(f(2, 32)*f(32, 76))
