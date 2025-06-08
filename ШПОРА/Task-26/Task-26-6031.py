with open('txt/26_6031.txt') as file:
    n = int(file.readline())
    circles = sorted([int(i) for i in file], reverse=True)
selected = [circles[0]]
for i in circles:
    if selected[-1] - i >= 6:
        selected.append(i)
print(len(selected), selected[-1])
