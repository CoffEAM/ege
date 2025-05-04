def f(a):
    for x in range(1, 10000):
        u = (a % 12 == 0) and ((530 % x == 0) <= ((a % x != 0) <= (170 % x != 0)))
        if not u:
            return False
    return True

ans = 0
for a in range(1, 1001):
    if f(a):
        ans += 1
print(ans)
