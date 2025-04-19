from itertools import *

ans = 0
for i in range(1, 11):
    for num in permutations('0123456789', i):
        num = ''.join(num)
        if num[0] != '0' and int(num) % 5 == 0:
            ans += 1
print(ans)
