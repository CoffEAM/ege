from re import finditer

with open('txt/24-347.txt') as file:
    st = file.readline()

pattern = r'[1-9AB][0-9AB]*[02468A]'
res = [i.group() for i in finditer(pattern, st)]
ans = 0
arr = []
for i in res:
    if int(i, 12) % 6 == 0:
        ans = max(ans, len(i))
    else:
        for a1 in range(len(i)):
            for a2 in range(len(i), a1, -1):
                l = i[a1:a2]
                if l[0] != '0':
                    if int(l, 12) % 6 == 0:
                        ans = max(ans, len(l))
                        break
print(ans)
k = '90652045783692100768059412303197502468003247859610086145293703192806457014290756380289541370601760259843016'
print(st.find(k) + 106)
