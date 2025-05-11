with open('txt/26_9847.txt') as file:
    N = file.readline()
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
vis = []
print(data)
for time in range(1350):
    suum = 0
    for visitor in data:
        if visitor[0] <= time <= visitor[1]:
            suum += 1
    vis.append(suum)
for i in vis:
    if i == max(vis):
        print(vis.index(i))
print(vis[730:750])
