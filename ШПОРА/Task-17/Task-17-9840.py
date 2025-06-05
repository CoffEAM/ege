with open('txt/17_9840.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '39'])
ans = []
for i in range(len(data) - 1):
    p = data[i:i+2]
    u = sum(1 for j in p if len(str(abs(j))) == 4)
    if u == 1 and sum(p) ** 2 <= maxx**2:
        ans.append(sum(p))
print(len(ans), max(ans))
