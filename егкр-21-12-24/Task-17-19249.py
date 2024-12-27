with open("A:/Загрузки/17_19249.txt") as file:
    data = file.readlines()

arr = [[data[i][:-1], data[i + 1][:-1], data[i + 2][:-1]] for i in range(len(data) - 2)]
maxx = max([int(i[:-1]) for i in data if len(i[:-1]) == 5 and i[:-1][-2:] == '43'])

ans = []
for i in arr:
    cnt = 0
    k = 0
    for j in i:
        if len(j) == 5 and j[-2:] == '43':
            cnt += 1
        k += int(j) ** 2
    if cnt > 0 and k <= maxx ** 2:
        ans.append(k)

#Ошибка как я понял в цикле, неверное количество троек последовательности, ошибку не нашел
print(len(ans), min(ans))



