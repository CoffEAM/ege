def f(x, y, s):
    if x + y >= 175: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, y, s - 1),
        f(x * 3, y, s - 1),
        f(x, y + 1, s - 1),
        f(x, y * 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 155) if f(19, s, 2)][0])
print([s for s in range(1, 155) if f(19, s, 3) and not f(19, s, 1)][0])
print([s for s in range(1, 155) if f(19, s, 4) and not f(19, s, 2)][0])
