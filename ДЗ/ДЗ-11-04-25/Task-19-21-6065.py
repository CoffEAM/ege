def f(x, s, hod1=False, hod2=False, hod3=False):
    if x > 40: return s % 2 == 0
    if s == 0: return False
    h = [f(x + 3, s - 1), f(x + 6, s - 1), f(x * 2, s - 1)]
    if hod1:
        h = [f(x + 6, s - 1, False, True), f(x * 2, s - 1, False, False,True)]
    if hod2:
        h = [f(x + 3, s - 1, True), f(x * 2, s - 1, False, False,True)]
    if hod3:
        h =     [f(x + 3, s - 1, True), f(x + 6, s - 1, False, True)]
    return any(h) if (s - 1) % 2 == 0 else all(h)


print(max([s for s in range(2, 37) if f(s, 2)]))
print(max([s for s in range(2, 27) if f(s, 3) and not f(s, 1)]))
print(min([s for s in range(2, 27) if f(s, 4) and not f(s, 2)]))
