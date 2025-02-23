def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        if x != 30:
            return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
        else:
            return 0

print(f(10, 60)*f(60, 70)) # --- 40+55
