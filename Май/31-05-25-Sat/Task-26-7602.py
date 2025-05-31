with open('txt/26_7602.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
cels = [0] * K
cnt = 0
last_cel = 0
for i in data:
    for c in range(K):
        if i[0] >= cels[c]:
            cels[c] = i[1] + 1
            last_cel = c + 1
            cnt += 1
            break
print(cnt, last_cel)
