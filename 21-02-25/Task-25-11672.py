from fnmatch import fnmatch

for i in range(21025, 10**10, 21025):
    if fnmatch(str(i), '12*34?5'):
        cnt_c = sum(1 for i in str(i) if int(i)%2==0)
        cnt_n = sum(1 for i in str(i) if int(i)%2!=0)
        if cnt_c==cnt_n:
            print(i, i//21025)

