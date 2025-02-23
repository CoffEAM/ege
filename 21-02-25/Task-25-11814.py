from fnmatch import fnmatch

for i in range(2100068079 - 2100068079%1777, 10**10, 1777):
    if i <= 2199968979:
        if fnmatch(str(i), '21*68?79'):
            print(i, i//1777)
