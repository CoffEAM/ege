with open('txt/17_11949.txt') as file:
    data = file.readlines()
data = [i[:-1] for i in data]
print(data[:10])
arr = [[data[i], data[i + 1], data[i + 2], data[i + 3]] for i in range(len(data) - 4)]
maxx = max(int(i) for i in data if i[-2:] == '68')
ans_count = 0
ans_sum = []
for i in arr:
    count = 0
    summ = 0
    for j in i:
        if len(j) == 2 and j[0] != '-':
            count += 1
        elif j[0] == '-' and len(j) == 3:
            count += 1
        summ += int(j)
    if count == 1 or count == 4:
        if summ >= maxx:
            ans_count += 1
            ans_sum.append(summ)
print(ans_count, max(ans_sum))


