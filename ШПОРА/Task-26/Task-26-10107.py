with open('txt/26_10107.txt') as file:
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times, key=lambda x: (x[1], -x[0]))
approved = [times[0]]
for time in times:
    if approved[-1][1] <= time[0]:
        approved.append(time)
times = sorted(times, key=lambda x: -x[0])
approved.remove(approved[-1])
for time in times:
    if approved[-1][1] <= time[0]:
        approved.append(time)
        break
print(len(approved), approved[-1][0] - approved[-2][1])
