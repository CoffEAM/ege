def f(x, s):
    if x <= 19: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x - 2, s -1),
        f(x - 5, s - 1),
        f(x // 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print([s for s in range(20, 200) if f(s, 2)][0])
print([s for s in range(20, 200) if f(s, 3) and not f(s, 1)])
print([s for s in range(20, 200) if f(s, 4) and not f(s, 2)])
