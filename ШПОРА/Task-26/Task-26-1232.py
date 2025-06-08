with open('txt/26_1232.txt') as file:
    s, n = map(int, file.readline().split())
    files = sorted([int(i) for i in file])

selected = []
for i in files:
    if s - i >= 0:
        selected.append(i)
        s -= i
s += selected[-1]
selected.remove(selected[-1])
for i in files[::-1]:
    if s - i >= 0:
        selected.append(i)
        break
print(len(selected), selected[-1])
