def f(A):
    for x in range(100):
        for y in range(100):
            f = (x<A) or (y<A) or (x + 2*y > 50)
            if not f:
                return False
    return True

for A in range(100):
    if f(A):
        print(A)
        break
