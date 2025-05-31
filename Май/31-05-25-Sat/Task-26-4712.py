with open('txt/26_4712.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
ans = [data[0]]
for i in data:
    if ans[-1] - i >= 3:
        ans.append(i)
print(len(ans), ans[-1])
