with open(r'txt\26_8279.txt') as file:
    t, N, M = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file]

clients = sorted(data, key=lambda x: (-x[0], x[1], -x[2]), reverse=True)
clients = [i for i in clients if i[2] <= M]
print(clients)
