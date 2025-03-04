with open(r'txt\26_8279.txt') as file:
    t, N, M = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file]

clients = [i for i in data if i[2] <= M]
clients = sorted(clients, key=lambda x: (-x[0], x[1], -x[2]), reverse=True)

print(clients)
buy_items = []
for i in clients:
    summ = sum(1 for k in range(i[0] + i[0]%6, i[1]+1, 6))
    time = sum(1 for j in range(i[0], i[1]+1))
    buy_items.append([time , summ])

print(*max(buy_items))


