with open('txt/26_6641.txt') as file:
    N, M = map(int, file.readline().split())
    data = [list(i.split()) for i in file]

data = [[int(i[0]), i[1]] for i in data]
data = sorted(data)
cnt = 0
summ = []
for i in data:
    if M - i[0] >= 0:
        M -= i[0]
        cnt += 1
        summ += [i]
print(sum([1 for i in summ if i[1] == 'S']))
