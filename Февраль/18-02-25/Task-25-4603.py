from itertools import product

#100000000
st = '1234*7'
ans = []
for k in range(5):
    for val in product('0123456789', repeat=k):
        st = '1234' + ''.join(val) + '7'
        if int(st)%141==0 and int(st)<10**8:
            ans.append([int(st), int(st)//141])
for i in ans:
    print(*i)
