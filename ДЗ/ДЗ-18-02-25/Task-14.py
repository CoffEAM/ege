from string import digits, ascii_uppercase
alph = digits + ascii_uppercase
alph = alph[:25]

num = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 - 2*25**5 - 2024
res = ''
while num:
    res += alph[num%25]
    num //= 25
print(res.count('0'))
