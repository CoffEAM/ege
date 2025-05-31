with open('txt/26_6031.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
k = data[0]
ans = [data[0]]
for i in data:
    if k - i >= 6:
        k = i
        ans.append(i)
print(len(ans), ans[-1])
