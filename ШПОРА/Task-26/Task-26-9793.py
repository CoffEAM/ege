with open('txt/26_9793.txt') as file:
    n = int(file.readline())
    details = []
    for pos, i in enumerate(file, start=1):
        i = list(map(int, i.split()))
        details.append([pos, i[0], i[1], i[0]+i[1]])

details = sorted(details, key=lambda x: x[3])
arr = []
for i in details:
    arr.append([i[0], i[1], 0]) #шлифовка
    arr.append([i[0], i[2], 1]) #окрашивание
line = [[0]] * n
print(arr)
cnt = 0
for i in range(n*2):
    num, stat = arr[i][0], arr[i][2]
    if stat == 1:
        if line[n - i//2 - 1] == 0:
            line[n - i//2 - 1] = [num, stat]
    if stat == 0:
        if line[i//2] == [0]:
            line[i//2] = [num, stat]
    if [0] not in line:
        print(arr[i][0])
        break
print(line)
