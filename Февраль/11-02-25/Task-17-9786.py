with open('txt/17_9786.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-2:]=='25'])
troiki = [[arr[i], arr[i + 1], arr[i + 2]] for i in range(len(arr) - 2)]
ans = []
for troika in troiki:
    k = 0
    for num in troika:
        if 999 < abs(num) < 10000:
            k += 1
    if k <= 2 and sum(troika) <= maxx:
        ans.append(sum(troika))
print(len(ans), max(ans))
