with open('txt/26_10107.txt') as file:
    n = int(file.readline())
    events = [list(map(int, i.split())) for i in file]

events = sorted(events, key=lambda x: (x[1], -x[0]))
approved = [events[0]]
for i in events:
    if approved[-1][1] <= i[0]:
        approved.append(i)
print(len(approved), approved[-1][0] - approved[-2][1])
