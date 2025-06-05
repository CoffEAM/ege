with open('txt/17_17680.txt') as file:
    data = [int(i) for i in file]

minn = min([i for i in data if i > 0 and i % 41 == 0])
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    if len(set(p)) == 2 and abs(p[0] - p[1]) % minn == 0:
        ans.append(sum(p))
print(len(ans), max(ans))
