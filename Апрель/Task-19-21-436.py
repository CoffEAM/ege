def f(x, y, s):
    if x + y >= 44: return s % 2 == 0
    if s == 0: return False
    h = [f(x + y, y, s - 1), f(x, x + y, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

# print([s for s in range(200) if f(11, s, 2)][0])
# print([s for s in range(200) if f(11, s, 3) and not f(11, s, 1)][0])
arr = []
for s1 in range(200):
    for s2 in range(200):
        if f(s1, s2, 3):
            arr.append([abs(s1-s2), s1, s2])
print(min(arr))
