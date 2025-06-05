with open('txt/17_17636.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-1] == '3' and len(str(abs(i))) == 3])
ans = []
for i in range(len(data) - 2):
    tr = data[i:i+3]
    u1 = sum(1 for j in tr if str(j)[-1] == '3' and len(str(abs(j))) == 3)
    if u1 >= 1 and sum(tr) < maxx:
        ans.append(sum(tr))
print(len(ans), max(ans))
