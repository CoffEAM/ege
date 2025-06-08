with open('txt/26_4604.txt') as file:
    n = int(file.readline())
    boxes = sorted([int(i) for i in file], reverse=True)

selected = [boxes[0]]
for box in boxes:
    if selected[-1] - box >= 3:
        selected.append(box)
print(len(selected), selected[-1])
