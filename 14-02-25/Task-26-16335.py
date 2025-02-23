with open('txt/26_16335.txt') as file:
    N = file.readline()
    diametrs = [int(i) for i in file]

diametrs = sorted(diametrs, reverse=True)
arr = [diametrs[0]]
for i in range(len(diametrs)):
    if arr[-1] - diametrs[i] >= 4:
        arr.append(diametrs[i])
print(len(arr), min(arr))

