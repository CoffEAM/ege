from itertools import product

err = [i*3 for i in '0123456789']
ans = 0
for i in product('0123456789', repeat=7):
    i = ''.join(i)
    if i[-1] not in '347':
        cnt = 0
        for k in err:
            if k in i:
                cnt += 1
        if not cnt:
            ans += 1
print(ans)
