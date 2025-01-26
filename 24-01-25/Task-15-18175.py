def delet(x, y):
    return 1 if x%y==0 else 0

def f(a):
    for x in range(1, 1000):
        f = (not(delet(x, 7)) and delet(x, 13)) <= (x > a - 40)
        if not f:
            return 0
    return 1

for a in range(1, 1000):
    if f(a):
        print(a)

