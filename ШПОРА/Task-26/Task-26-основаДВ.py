with open('txt/26_5988.txt') as file:
    n = int(file.readline())
    boxes = []
    for i in file:
        data = i.split()
        boxes.append([int(data[0]), data[1]])

boxes = sorted(boxes, reverse=True)
start1 = [max(boxes, key=lambda x: x[1] == 'R')]
start2 = [max(boxes, key=lambda x: x[1] == 'G')]
start3 = [max(boxes, key=lambda x: x[1] == 'B')]
for i in boxes:
    if start1[-1][0] - i[0] >= 7 and start1[-1][1] != i[1]:
        start1.append(i)
    if start2[-1][0] - i[0] >= 7 and start2[-1][1] != i[1]:
        start2.append(i)
    if start3[-1][0] - i[0] >= 7 and start3[-1][1] != i[1]:
        start3.append(i)
print(len(start1), len(start2), len(start3))
