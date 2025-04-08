with open('26.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
ans = [data[0]]
for i in data[1:]:
    if ans[-1] - i >= 9:
        ans.append(i)
print(len(ans), ans[-1])
