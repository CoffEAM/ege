with open('txt/24_8579.txt') as file:
    st = file.readline()

ans = 0
for i in range(len(st) - 1):
    for j in range(i, len(st)):
        r = st[i:j + 1]
        if r[0] in '0123456789' and r[-1] in '0123456789':
            if int(r[0]) % 2 != int(r[-1]) % 2:
                fg = True
                for k in '012356789':
                    if k != r[0] and k != r[-1]:
                        if r.count(k) != 0:
                            fg = False
                if fg:
                    ans = max(ans, len(r))
print(ans)
