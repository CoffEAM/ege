from fnmatch import fnmatch

for i in range(1021574 - 1021574%2024, 10**10, 2024):
    if fnmatch(str(i), '1?2157*4'):
        print(i, i//2024)
