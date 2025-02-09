for n in range(1, 10000):
    r = bin(n)[2:]
    if n%4==0:
        r += r
    else:
        r += r[::-1]
    r = int(r, 2)
    if r >= 544:
        print(n)
        break
#17


