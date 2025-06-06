with open('txt/17_9748.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-2:] == '15'])
ans = []
for i in range(len(data) - 2):
    tr = data[i:i+3]
    u = sum(1 for j in tr if len(str(j)) == 4)
    if u == 1 and sum(tr) >= maxx:
        ans.append(sum(tr))
print(len(ans), max(ans))
