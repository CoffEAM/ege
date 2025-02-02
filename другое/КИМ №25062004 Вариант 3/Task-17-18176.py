with open("txt/TXT-17-18176.txt") as file:
    data = file.readlines()
data = [i[:-1] for i in data]
arr = [[data[i], data[i + 1], data[i + 2]] for i in range(len(data) - 2)]
minn = min(int(i) for i in data if int(i) > 0 and i[-1] == '4')

cnt = 0
ans = []
for i in arr:
    for j in range(len(i) - 2):
        summ = 0
        for k in i[j] + i[j + 1] + i[j + 2]:
            if k != '-':
                summ += int(k)
        if summ == minn:
            cnt += 1
            ans.append(int(i[j])+int(i[j+1])+int(i[j+2]))

print(cnt, max(ans))
