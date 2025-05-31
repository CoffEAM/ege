with open('txt/26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    data = [i.split() for i in file]

data = [[int(i[0]), i[1]] for i in data]
data = sorted(data)
s = []
w = []
for i in data.copy():
    if i[0] <= M:
        M -= i[0]
        if i[1] == 'S': s.append(i[0])
        else: w.append(i[0])
        data.remove(i)

for i in data:
    if i[1] == 'S' and M + w[-1] - i[0] >= 0:
        M += w[-1] - i[0]
        s.append(i[0])
        w.pop()
print(len(s), M)

