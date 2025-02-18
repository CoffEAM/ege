def f(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        if x != 36 and x != 100:
            return f(x//2, y) + f(x//3, y) + f(x-3, y)
        else:
            return 0

print(f(163, 45)*f(45, 3))
