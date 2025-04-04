def f(x, y, s):
    if x + y >= 30: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 1, y, s - 1),
        f(x * 2, y, s - 1),
        f(x, y + 1, s - 1),
        f(x, y * 2, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

# u19 = []
# for s in range(1, 30):
#     for k in range(1, 30):
#         if f(k, s, 2) and s + k < 30:
#             if [s, k] not in u19:
#                 u19.append([s, k])
# print(len(u19))

# 19 -> 445

# u20 = [s for s in range(1, 30) if f(s, 6, 3) and not f(s, 6, 1)]
# print(u20[0], u20[-1])

# 20 -> 5 11

u21 = []
for s in range(1, 30):
    for k in range(1, 30):
        if f(s, k, 4) and s + k < 30 and not f(s, k, 2):
            if [s, k] not in u21:
                u21.append([s, k])
print(len(u21))
