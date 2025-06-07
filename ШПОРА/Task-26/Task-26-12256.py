with open('txt/26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    items = [int(i) for i in file]

items = sorted(items)
selected = []
for i in items:
    if s - i >= 0:
        selected.append(i)
        s -= i
print(len(selected))
s += max(selected)
selected.remove(max(selected))
for i in items[::-1]:
    if s - i >= 0:
        selected.append(i)
        break
print(max(selected))
