with open('txt/17_4622.txt') as file:
    data = [int(i) for i in file]

minn = min([i for i in data if i > 0 and i % 19 == 0])
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    if sum(p) < minn:
        ans.append(sum(p))
print(len(ans), abs(max(ans)))
