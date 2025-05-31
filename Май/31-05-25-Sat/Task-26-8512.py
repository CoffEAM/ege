with open('txt/26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
last_cel = 0
cnt = 0
cels = [0] * K
for time in times:
    for c in range(K):
        if time[0] >= cels[c]:
            cels[c] = time[1] + 1
            last_cel = c + 1
            cnt += 1
            break
print(cnt, last_cel)
