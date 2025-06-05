from string import ascii_uppercase, digits

alph = digits + ascii_uppercase

num = 4 * 3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
res = ''
while num:
    res += alph[num%25]
    num //= 25
ans = sum(1 for i in res if int(i, 25) > 10)
print(ans)
