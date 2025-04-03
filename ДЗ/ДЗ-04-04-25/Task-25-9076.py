from fnmatch import fnmatch

for i in range(2023, 10**9 + 1, 2023):
    suum = sum(map(int, str(i)))
    if fnmatch(str(i), '20*23') and suum % 7 == 0 and suum < 20:
        print(i)

