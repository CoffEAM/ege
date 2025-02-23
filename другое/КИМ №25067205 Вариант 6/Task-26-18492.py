with open('txt/26_18492.txt') as file:
    n = file.readline()
    trains = [list(map(int, i.split())) for i in file]

trains = sorted(trains, key=lambda x: x[1])
ans = []
for i in range(len(trains)):
    cnt = 1
    for j in range(i, len(trains)):
        if trains[i][2] > trains[j][1] and trains[i][1] < trains[j][2] and trains[i] != trains[j]:
            cnt += 1
    ans.append(cnt)
k = 0
for i in ans:
    if ans.count(i) > k:
        k = ans.count(i)
print(k)
