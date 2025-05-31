with open('txt/26_1207.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

summ = []
data = sorted(data)
for i in data:
    if sum(summ) + i <= S:
        summ.append(i)
summ.remove(max(summ))
for i in data[::-1]:
    if sum(summ) + i <= S:
        print(len(summ) + 1, i)
        break
