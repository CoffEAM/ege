def c(num):
    res = set()
    for i in range(1, int(num**0.5) + 1):
        if num %i==0:
            res |= {i, num//i}
    return sum(res)

def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    return f(x + 1, y) + f(c(x), y)

print(f(2, 24))
