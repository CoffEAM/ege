with open('txt/17_9748.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-2:]=='15'])
troiki = [[arr[i], arr[i+1], arr[i+2]] for i in range(len(arr)-2)]
cnt = 0
summs = []
for troika in troiki:
    k = 0
    for num in troika:
        if 1000<= num <= 9999:
            k += 1
    if k == 1 and sum(troika)>=maxx:
        cnt += 1
        summs.append(sum(troika))
print(cnt, max(summs))
