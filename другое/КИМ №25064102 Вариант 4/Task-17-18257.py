with open('txt/17_18257.txt') as file:
    data = file.readlines()
data = [i[:-1] for i in data]
maxx = max(int(i) for i in data)
arr = [list(i) for i in enumerate(data, start=1)]
arr = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
print(arr[:20])
cnt = 0
ans = []
for i in arr:
    for j in range(len(i)-1):
        summ = i[j][0] + i[j+1][0]
        summ_e = int(i[j][1]) + int(i[j + 1][1])
        if str(summ)[-1] == str(maxx)[-1]:
            cnt += 1
            ans.append(abs(summ_e - summ))
print(cnt, min(ans))

