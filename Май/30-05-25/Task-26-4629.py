with open('txt/26_4629.txt') as file:
    N = int(file.readline())
    data = [int(i) for i in file]

data = sorted(data)
summ1 = sum(data[:len(data)//4])/2 + sum(data[len(data)//4:])
data = sorted(data, reverse=True)
summ2 = sum(data[:len(data)//4])/2 + sum(data[len(data)//4:])
print(summ2, summ1)
