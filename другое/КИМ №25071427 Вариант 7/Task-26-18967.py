with open('txt/26_18967.txt') as file:
    N, K = list(map(int, file.readline().split()))
    clients = [list(map(int, i.split())) for i in file]

clients = sorted(clients, key=lambda x: x[1])
clothes = []
ans = 0
timeline = [i for i in range(1500)]
for client in clients:
    if N > client[2]:
        if client[0] not in clothes:
            N -= client[2]
            clothes.append(client[0])
        else:
            N += client[2]
            clothes.remove(client[0])
    else:
        ans += 1
print(ans)
