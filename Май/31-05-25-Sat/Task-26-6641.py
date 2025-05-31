with open('txt/26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    data = [i.split() for i in file]

data = [[int(i[0]), i[1]] for i in data]
data = sorted(data)
print(data)
