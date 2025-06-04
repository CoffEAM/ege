from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[:21]:
    num = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if num % 20 == 0:
        print(num//20)
        break
