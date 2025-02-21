from fnmatch import fnmatch

for i in range(1021574 - 1021574%133, 10**10, 133):
    if str(i)[1] in '02468':
        if fnmatch(str(i), '1?2157*4'):

