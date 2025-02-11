for num in range(800001, 9000001):
    r = 0
    for delitel in range(1, num//2):
        if num%delitel==0:
            r += delitel
    if str(r)[-1]=='3':
        print(num, r)

#800004 682713
#800024 300023
#800064 1157023
#800068 200023
#800084 211073

