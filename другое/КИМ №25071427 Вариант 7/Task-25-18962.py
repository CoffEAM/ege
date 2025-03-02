from fnmatch import fnmatch

for num in range(500001, 3000000):
    for delitel in range(1, num//2):
        if num%delitel == 0:
            if fnmatch(str(delitel), '2*3?'):
                print(num, delitel)
