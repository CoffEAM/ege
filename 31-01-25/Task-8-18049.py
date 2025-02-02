from itertools import product

st = '012345678'
arr = [i*3 for i in st]
cnt = 0
for num in product('012345678', repeat=7):
    num = ''.join(num)
    if num[0] not in '0246':
        flag = 0
        for k in arr:
            if k == num[-3:]:
                flag += 1
        if flag==0:
            cnt += 1
print(cnt)


