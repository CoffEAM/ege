from fnmatch import fnmatch

ans = []
for i in range(1746008 - 1746008%86513, 10**12+1, 86513):
    if fnmatch(str(i), '17*46??8'):
        suum = sum(int(k) for k in str(i))
        if int(suum ** 0.5) == suum**0.5:
            ans.append([i, i//86513])

for i in ans:
    print(*i)
