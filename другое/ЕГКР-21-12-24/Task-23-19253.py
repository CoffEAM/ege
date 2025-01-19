def f(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        if x != 24:
            return f(x-1, y) + f(x-6, y) + f(x//2, y)
        else:
            return 0

print(f(34, 29)*f(29,19)*f(19,6))

