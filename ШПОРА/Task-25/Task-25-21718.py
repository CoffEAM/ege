from fnmatch import fnmatch

for i in range(447361 - 447361%7993, 10**10, 7993):
    if fnmatch(str(i), '4*4736*1'):
        print(i, i // 7993)
