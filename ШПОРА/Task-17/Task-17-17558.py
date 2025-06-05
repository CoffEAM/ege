with open('txt/17_17558.txt') as file:
    data = [int(i) for i in file]

cnt = sum(1 for i in data if i % 32 == 0)
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    u = sum(1 for j in p if j < 0)
    if u >= 1 and sum(p) < cnt:
        ans.append(sum(p))
print(len(ans), max(ans))
