with open('txt/26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file]

for i in data:
    i.append(sum(i[1:]))
data = sorted(data, key=lambda x: -x[-1])
r = data[:1076]
r = sorted(r, key=lambda x: (-x[-1], -x[-2], x[0]))
cnt = sum(1 for i in r if i[-1] == 279)
cnt1 = sum(1 for i in data if i[-1] == 279)
print(cnt, cnt1)
