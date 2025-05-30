with open('txt/26_3230.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, key=lambda x: (-x[0], x[1]))
for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0]:
        if data[i + 1][1] - data[i][1] - 1 == 11:
            print(data[i][0], data[i][1] + 1)
            break
