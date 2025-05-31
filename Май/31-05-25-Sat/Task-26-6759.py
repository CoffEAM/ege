with open('txt/26_6759.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
sum1 = sum([data[i] for i in range(N) if (i + 1) % 3 != 0])
data = data[::-1]
sum2 = sum(data[int(N/3):])
print(sum2, sum1)
