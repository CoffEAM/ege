from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:15]

num = 3*15**1140 + 2*15**1025 + 15**923 - 3*15**85 + 2*15**74 + 3
res = ''
while num:
    res += alph[num%15]
    num //= 15
print(res)
cnt = 1
counts = []
for i in range(len(res)-1):
    if res[i] == res[i+1]:
        cnt += 1
    else:
        counts.append(cnt)
        cnt = 1
print(max(counts))
print(res.count('E'))
