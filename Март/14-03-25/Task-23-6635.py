"""1111"""
def f(x, cnt=0):
    if cnt == 13 and x < 0:
        ans.append(x)
        return 1
    if cnt == 13 and x >= 0:
        return 0
    return f(x -3 , cnt + 1) + f(x * (-3), cnt + 1)

ans = []
print(f(333), len(set(ans)))

'''2222'''
def g(x, cnt=0):
    if cnt == 13 and x < 0:
        return [x]
    if cnt == 13 and x >= 0:
        return []
    return g(x -3 , cnt + 1) + g(x * (-3), cnt + 1)

print(len(set(g(333))))
