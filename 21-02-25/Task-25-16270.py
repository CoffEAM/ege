st = '12?345?67089?'
for i in '0123456789':
    for k in '0123456789':
        for l in '0123456789':
            num = f'12{i}345{k}67089{l}'
            if int(num)<=10**13 and int(num)%206==0:
                print(num, int(num)//206)
