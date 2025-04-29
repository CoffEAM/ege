from itertools import permutations

ch = [i+j for i in '0246' for j in '0246']
nech = [i+j for i in '1357' for j in '1357']

ans = 0
for i in permutations('01234567', 6):
    i = ''.join(i)
    u1 = sum(1 for k in ch if k in i)
    u2 = sum(1 for j in nech if j in i)
    if u1 + u2 == 0 and int(i, 8) % 5 == 0 and i[0] != '0':
        ans += 1
print(ans)
