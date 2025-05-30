with open('txt/26_4604.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
ans = [data[0]]
k = data[0]
for i in data[1:]:
    if k - i >= 3:
        ans.append(i)
        k = i
print(len(ans), ans[-1])
