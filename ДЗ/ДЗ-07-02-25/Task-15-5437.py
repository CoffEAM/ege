from itertools import combinations

def delet(n, m):
    return 1 if n%m==0 else 0

def f(x, y, z, a):
    return (delet(z, 115) or delet(y, 78) or delet(x, 51)) <= delet(x, a)

ans = []
for a_a in range(1, 100):
    for y_y in range(1, 100):
        for z_z in range(1, 100):
            if all(f(x_x, y_y, z_z, a_a) for x_x in range(1, 100)):
                ans.append(a_a)
print(max(ans))


