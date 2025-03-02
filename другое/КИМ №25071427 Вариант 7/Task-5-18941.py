for num in range(1000, 10000):
    digit1 = str(num)[0]
    comp = []
    for digit in str(num)[1:]:
        comp.append(str(int(digit1)*int(digit)))
    comp = sorted(comp)
    res = comp[-2]+comp[-1]
    if res == '5472':
        print(num)
        break
