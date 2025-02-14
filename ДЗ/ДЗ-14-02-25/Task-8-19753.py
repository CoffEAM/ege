from itertools import product

cnt = 0
for num in range(100000, 1000000):
    if num%4==0 and len(set(str(num))) == len(str(num)):
        u = 0
        for k in product('02468', repeat=2):
            k = ''.join(k)
            if k in str(num):
                u += 1
        if u == 0:
            cnt += 1
print(cnt)
