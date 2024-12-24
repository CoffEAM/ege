def convert(num):
    res = ''
    while num:
        res += str(num%3)
        num //= 3
    return res[::-1]


ans = []
for n in range(1, 10000):
    r = convert(n)
    if n%3==0:
        r = r + r[-2:]
    else:
        r = r + convert(sum(map(int, r)))
    r = int(r, 3)
    if r%2==0 and r>220:
        ans.append(r)
print(min(ans))







