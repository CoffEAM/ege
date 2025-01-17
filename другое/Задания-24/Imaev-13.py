from string import ascii_uppercase

alph = ascii_uppercase

st = open('imaev/24-s1.txt').readlines()

cnt = 0
for i in st:
    for k in alph:
        if f'C{k}B' in i:
            cnt += 1
            break
print(cnt)
