from itertools import product

st = '6*97*5?'
ans = []
for i in '0123456879':
    st ='6*97*5'+ i
    for k in range(0, 3):
        for val in product('0123456789', repeat=k*2):
            val = ''.join(val)
            st = '6' + val[:len(val)//2] + '97' + val[len(val)//2:] + f'5{i}'
            cnt = 0
            summ = 0
            for g in range(1, 100):
                if g%2==0 and int(st)%g==0:
                    cnt += 1
                    summ += g
            if cnt>=4:
                ans.append([st, summ])
print(ans[:30])

