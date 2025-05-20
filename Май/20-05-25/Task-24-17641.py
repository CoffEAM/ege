from re import finditer

with open('txt/24_17641.txt') as file:
    st = file.readline()

chislo = r'([1-9][0-9]*|0)'
pattern = fr'{chislo}([+*]{chislo})*'
res = [i.group() for i in finditer(pattern, st)]
ans = 0
for i in res:
    if eval(i) == 0:
        ans = max(ans, len(i))
    else:
        for j in range(len(i) + 1):
            for k in range(len(i), j, -1):
                s = i[j:k].strip('+*')
                if s:
                    if s[0] == '0' and len(s) > 1:
                        if s[1] not in '0123456789':
                            if eval(s) == 0:
                                ans = max(ans, len(s))
                        else:
                            break
                    else:
                        if eval(s) == 0:
                            ans = max(ans, len(s))
print(ans)
