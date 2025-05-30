with open('txt/26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

summ = []
data = sorted(data)
for i in data:
    if i <= S:
        S -= i
        summ.append(i)
S += summ.pop()
for i in data[::-1]:
    if i <= S:
        summ.append(i)
        break
print(len(summ), summ[-1])
