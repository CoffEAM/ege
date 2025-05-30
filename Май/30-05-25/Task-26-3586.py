with open('txt/26_3586.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (-x[0], x[1]))
maxx = 0
for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0]:
        maxx = max(data[i + 1][1] - data[i][1] - 1, maxx)
for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0]:
        if data[i + 1][1] - data[i][1] - 1 == maxx:
            print(data[i][0])
            break
print(maxx)
