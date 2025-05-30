with open('txt/26_2944.txt') as file:
    S, N = map(int, file.readline().split())
    data = [int(i) for i in file]

summ = []
data = sorted(data)
for i in data:
    if sum(summ) + i <= S:
        summ.append(i)
print(len(summ))
summ.remove(max(summ))
for i in data[::-1]:
    if sum(summ) + i <= S:
        print(i)
        break
