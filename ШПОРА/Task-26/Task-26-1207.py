with open('txt/26_1207.txt') as file:
    s, n = map(int, file.readline().split())
    files = sorted([int(i) for i in file])

selected = []
for i in files:
    if s - i >= 0:
        s -= i
        selected.append(i)
s += selected[-1]
selected.remove(selected[-1])
for i in files[::-1]:
    if s - i >= 0:
        selected.append(i)
        break
print(len(selected), selected[-1])
