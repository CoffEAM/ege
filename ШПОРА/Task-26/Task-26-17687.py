with open('txt/26_17687.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data, reverse=True)
sum1 = sum(data[i] for i in range(N) if (i + 1) % 9 != 0)
sum2 = sum(data[N//9:])
print(sum1, sum2)
