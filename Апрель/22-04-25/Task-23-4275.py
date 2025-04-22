def f(x, y, cnt=0):
    if x == y and cnt <= 3: return 1
    elif x > y: return 0
    return f(x + 2, y, cnt) + f(x * 3, y, cnt + 1) + f(x * 5, y, cnt + 1)

print(f(2, 200))
