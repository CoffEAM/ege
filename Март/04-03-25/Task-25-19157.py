from fnmatch import fnmatch

for i in range(1035954 - 1035954%6437, 10**10, 6437):
    if fnmatch(str(i), '1?3*5*954'):
        print(i, i//6437)
