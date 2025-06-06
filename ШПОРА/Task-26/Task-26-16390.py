with open('txt/26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)
ans = []
for i in data:
    if S - i >= 0:
        S -= i
        ans.append(i)
print(len(ans), ans[-1])
S = S + ans[-1]
ans.remove(ans[-1])
data = sorted(data, reverse=True)
for i in data:
    if S - i >= 0:
        ans.append(i)
        break
print(ans[-1])
