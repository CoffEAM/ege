from itertools import product

for pos, num in enumerate(product('0123456789', repeat=5), start=1):
    num = ''.join(num)
    if num[0] != '0':
        for i in '02468':
            num = num.replace(i, '*')
        for i in '13579':
            num = num.replace(i, '+')
        if num.count('**') == 0 and num.count('++') == 0 and pos % 15 == 0:
            print(pos, num)
