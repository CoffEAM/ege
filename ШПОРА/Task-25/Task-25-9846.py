from fnmatch import fnmatch

for i in range(123405 - 123405%2025, 10**8, 2025):
    if fnmatch(str(i), '12*34?5'):
        print(i, i//2025)
