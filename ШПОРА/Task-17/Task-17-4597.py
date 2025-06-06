with open('txt/17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    u = sum(1 for k in p if k % 117 == minn)
    if u >= 1:
        ans.append(sum(p))
print(len(ans), max(ans))
