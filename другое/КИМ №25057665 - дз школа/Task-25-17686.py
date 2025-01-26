# 40
# 1 2 4 5 8 10 20 40

for n in range(700001, 1000000):
    for delitel in range(17, n//2):
        if n%delitel == 0 and str(delitel)[-1]=='7':
            print(n, delitel)



