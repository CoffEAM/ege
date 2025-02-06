from string import digits, ascii_uppercase
alph = digits+ascii_uppercase
def con(num):
    res = ''
    while num:
        res += alph[num%12]
        num //= 12
    return res[::-1]
ans = []
for n in range(1, 10000):
    r = con(n)
    if n%3==0:
        r = '1' + r + 'B'
    else:
        r = '2' + r + '0'
    r = int(r, 12)
    if r < 1996:
        ans.append(r)
print(max(ans))



