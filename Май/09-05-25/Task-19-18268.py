def f(x, y, s):
    if x + y <= 72: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x - 3, y, s - 1),
        f(x - x // 2, y, s - 1),
        f(x, y - 3, s - 1),
        f(x, y - y // 2, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print([s for s in range(23, 500) if f(50, s, 2)]) # 94
print([s for s in range(23, 500) if f(50, s, 3) and not f(50, s, 1)])
print([s for s in range(23, 500) if f(50, s, 4) and not f(50, s, 2)])
