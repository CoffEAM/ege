for n in range(10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r.replace('1', '11')
    else:
        r = r.replace('0', '00')
    r = int(r, 2)
    if r > 70:
        print(n)
        break

# Ответ 14
