from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

for x in alph[1:35]:
    num = int(f'6{x}QR{x}', 35) + int(f'{x}59SH', 35) + int(f'PH{x}69YW', 35)
    cnt = []
    for i in str(num):
        cnt.append([str(num).count(i), i])
    if num % int(max(cnt)[1]) ** 2 == 0:
        print(num // int(max(cnt)[1]) ** 2)
