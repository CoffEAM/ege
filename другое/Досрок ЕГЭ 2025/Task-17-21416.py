with open('txt/17_21416.txt') as file:
    data = [int(i) for i in file]

summ = sum(i for i in data if i < 0)
ans = []
for i in range(len(data) - 2):
    tr = data[i:i+3]
    if max(tr) * min(tr) > summ:
        ans.append(sum(tr))
print(len(ans), abs(max(ans)))
