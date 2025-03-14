def f(x, y, cnt=0):
    if x == y and cnt == 51: return 1
    elif x > y: return 0
    return f(x * 4, y, cnt + 1) + f(x + 1, y, cnt + 1) + f(x * 3, y, cnt + 1)

print(f(2, 404))

