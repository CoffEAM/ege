from itertools import product

ans = 0
for val in set(product('ДИОНИСИЙ', repeat=6)):
    val = ''.join(val)
    if val.count('Д') + val.count('Н') == 1:
        cnt = 0
        for par in range(len(val) - 1):
            if val[par] == val[par+1]:
                cnt += 1
        if cnt == 0:
            ans += 1
print(ans)
