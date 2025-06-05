from string import ascii_uppercase, digits

alph = digits + ascii_uppercase

for x in alph[:19]:
    num = int(f'98{x}79641', 19) + int(f'36{x}14', 19) + int(f'73{x}4', 19)
    if num % 18 == 0:
        print(num // 18)
