def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        if x!=16:
            return f(x + 2, y) + f(x * 3, y) + f(x * 2, y)
        else:
            return 0


print(f(13, 45))
