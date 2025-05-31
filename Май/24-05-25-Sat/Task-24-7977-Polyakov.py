from re import finditer

def f(s):
    summ = 0
    s = s.split('+')
    for i in s:
        mult = 1
        for j in i.split('*'):
            mult *= int(j, 6)
        summ += mult
    return summ

with open('txt/24-314.txt') as file:
    st = file.readline()

pattern = r'([1-5][0-5]*|0)([+*]([1-5][0-5]*|0))+'
res = [i.group() for i in finditer(pattern, st)]
ans = 0
for i in res:
    ans = max(ans, f(i))
print(f(max(res, key=lambda x: (len(x), f(x)))))
