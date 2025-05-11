from string import ascii_uppercase, digits

alph = digits + ascii_uppercase
for x in alph[:16]:
    for y in alph[:16]:
        num = int(f'27A{x}23', 16) + int(f'8{y}E5D2', 16)
        if num % 5 == 0:
            print(int(x + y, 16))
