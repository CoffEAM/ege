with open('txt/26var03.txt') as file:
    N, M, K = list(map(int, file.readline().split()))
    coordinates = [list(map(int, i.split())) for i in file.readlines()]

for i in range(1, K+1):
    coordinates.append([0, i])

maxx = []
for row in range(M, 0, -1):
    for column in range(1, K+1):
        if [row, column] in coordinates:
            maxx.append([-1, row, column])
        if [row, column] not in coordinates:
            cnt2 = 0
            for analiz in range(row-1, -1, -1):
                if [analiz, column] not in coordinates:
                    cnt2 += 1
                else:
                    maxx.append([cnt2, row, column])
                    break
print(max(maxx, key=lambda x: (x[0], -x[1], -x[2])))





