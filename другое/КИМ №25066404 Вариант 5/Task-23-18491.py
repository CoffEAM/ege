def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+3, y) + f(x + max([int(i) for i in str(x)]), y)

print(f(10, 24)*f(24, 41))

