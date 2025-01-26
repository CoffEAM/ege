from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:22]:
    num = int(f'A23{x}AC0', 22) + int(f'GB{x}21670', 22)
    if num%21==0:
        print(num//22)

