from string import digits, ascii_uppercase

alph = digits+ascii_uppercase

for x in range(1, 150):
    num = int(f'51{x}29') + int(f'{x}023')
    if num%149==0:
        print(num//149)


