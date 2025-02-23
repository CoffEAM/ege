from itertools import product
#100000000
ans = []
st = '12*4?65'
for l in '0123456789':
    for k in range(3):
        for val in product('0123456789', repeat=k):
            st = f'12{''.join(val)}4{l}65'
            if int(st)%161==0 and int(st)<10**8:
                ans.append([int(st), int(st)//161])
for i in sorted(ans):
    print(*i)
