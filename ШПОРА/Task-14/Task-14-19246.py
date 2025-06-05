from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:25]:
    num = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if num % 24 == 0:
        print(num//24)
