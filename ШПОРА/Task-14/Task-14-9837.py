from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:23]:
    num = int(f'7{x}38596', 23) + int(f'14{x}36', 23) + int(f'61{x}7', 23)
    if num % 22 == 0:
        print(num // 2)
        break
