from itertools import product
# l = 0 -> p in [0,1,2]       range = 3
# l = 1 -> p in [0, 1]        range = 2
# l = 2 -> p in [0]           range = 1

ans = []
for l in range(3):
    for p in range(3 - l):
        for k1 in product('0123456789', repeat=l):
            for k2 in product('0123456789', repeat=p):
                num = int(f'124{''.join(k1)}5{''.join(k2)}79')
                sum_n = sum(int(i) for i in str(num) if int(i)%2==1)
                if num % sum_n==0:
                    ans.append([num, sum(map(int, str(num)))])

for i in sorted(ans):
    print(*i)
