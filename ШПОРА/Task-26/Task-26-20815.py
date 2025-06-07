with open('txt/26_20815.txt') as file:
    n, k = map(int, file.readline().split())
    candidates = []
    for i in file:
        inf = list(map(int, i.split()))
        candidates.append([inf[0], sum(inf[1:]), inf[-1]])
candidates = sorted(candidates, key=lambda x: (-x[1], -x[2], x[0]))
selected = candidates[:k]
print(selected[-1])
cnt = 0
for i in candidates:
    if i[1] == 279:
        cnt += 1
print(cnt)
for i in selected:
    if i[1] == 280:
        print(i[0])