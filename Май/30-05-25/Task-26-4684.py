with open('txt/26_4684.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
summ1 = sum(data[:N//6])/2 + sum(data[N//6:])
data = sorted(data, reverse=True)
summ2 = 0
k = data[0]
for i in range(N):
    if (i + 1) % 6 == 0:
        summ2 += data[i] / 2
    else:
        summ2 += data[i]
    k = data[i]
print(int(summ2), int(summ1))
