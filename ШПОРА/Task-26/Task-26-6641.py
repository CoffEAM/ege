with open('txt/26_6641.txt') as file:
    n, m = map(int, file.readline().split())
    data = []
    for i in file:
        inf = i.split()
        data.append([int(inf[0]), inf[1]])

data = sorted(data)
s = []
w = []
for i in data.copy():
    if i[0] <= m:
        m -= i[0]
        if i[1] == 'S': s.append(i[0])
        else: w.append(i[0])
        data.remove(i)

for i in data:
    if i[1] == 'S' and m + w[-1] - i[0] >= 0:
        m += w[-1] - i[0]
        s.append(i[0])
        w.pop()
print(len(s), m)
