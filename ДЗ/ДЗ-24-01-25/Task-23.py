def f(x, y):
    if x>y:
        return 0
    if x==y:
        return 1
    if x<y:
        return f(x+2, y) + f(x + max(map(int, str(x))), y)

print(f(32, 55)*f(55, 76))


