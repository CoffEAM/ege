def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        if x != 12:
            return f(x + 1, y) + f(x+2, y) + f(x*3, y)
        else:
            return 0

print(f(2, 9)*f(9, 19))
