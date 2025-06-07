with open('txt/26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    candidates = []
    for i in file:
        inf = list(map(int, i.split()))
        inf.append(sum(inf[1:4]))
        candidates.append(inf)

candidates = sorted(candidates, key=lambda x: (-x[-1], -x[-2], x[0]))
selected = []
for candidate in candidates:
    if len(selected) < s:
        selected.append(candidate)
        s -= 1
print(selected[-1])
