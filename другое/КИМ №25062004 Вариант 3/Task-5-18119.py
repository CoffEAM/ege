def convert(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]


ans = []
for n in range(1, 10000):
    r = convert(n)
    if sum(map(int, r))%2 == 0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'
    r = int(r, 3)
    if r > 100:
        ans.append(r)
print(min(ans))
