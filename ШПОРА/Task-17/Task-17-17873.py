with open('txt/17_17873.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    u = sum(1 for j in p if j % 16 == minn)
    if u >= 1:
        ans.append(sum(p))
print(len(ans), max(ans))
