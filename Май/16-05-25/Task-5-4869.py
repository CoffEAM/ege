for n in range(2, 10000):
    r = bin(n)[2:]
    cnt1 = sum(1 for i in range(1, len(r), 2) if r[i] == '1')
    cnt2 = sum(1 for i in range(0, len(r), 2) if r[i] == '0')
    r = abs(cnt1 - cnt2)
    if r == 5:
        print(n)
        break

