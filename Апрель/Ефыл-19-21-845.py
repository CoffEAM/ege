def f(x, s):
    if 36 <= x <= 60: return s % 2 == 0
    elif x > 60: return (s - 1) % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, s - 1),
        f(x * 2, s - 1),
        f(x * 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print([s for s in range(1, 36) if f(s, 2)][0])
print(len([s for s in range(1, 36) if f(s, 3) and not f(s, 1)]))
u21 = [s for s in range(1, 36) if f(s, 4) and not f(s, 2)]
print(u21[0], u21[-1])
