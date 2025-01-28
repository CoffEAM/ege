from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in range(149, 0, -1):
    num1 = f'51{x}29'
    num2 = f'{x}023'
    num1_rever = num1[::-1]
    for i in range(len(num1)):
        num1 = num1[i*(-1)] * 150 ** num1_rever.index(num1[-1*i])
    num2 = (int(num2[-1])
            + int(num2[-2]) * 150 + int(num2[-3]) * 150 ** 2
            + int(num2[-4]) * 150 ** 3
            + int(num2[-5]) * 150 ** 4
            + int(num2[-6]) * 150 ** 5)
    print(num1)
    num = num1 + num2
    if num%149==0:
        print(num//149)

