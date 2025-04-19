def f(a):
    for x in range(-300, 300):
        for y in range(-300, 300):
            u = ((a < x) or (x ** 2 - 7 * x + 10 > 0)) and \
                ((a >= y) or (y ** 2 + 7 * y + 12 > 0))
            if not u:
                return False
    return True
ans = 0
for a in range(-300, 300):
    if f(a):
        ans += 1
print(ans)
