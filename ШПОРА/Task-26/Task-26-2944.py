with open('txt/26_2944.txt') as file:
    s, n = map(int, file.readline().split())
    files = sorted([int(i) for i in file])

selected = []
for file in files:
    if s - file >= 0:
        selected.append(file)
        s -= file
s += selected[-1]
selected.remove(selected[-1])
for file in files[::-1]:
    if s - file >= 0:
        selected.append(file)
        break
print(len(selected), selected[-1])
