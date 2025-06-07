with open('txt/26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    candidates = []
    for i in file:
        arr = list(map(int, i.split()))
        summ = sum(arr[1:-1])
        arr.append(summ)
        candidates.append(arr)
candidates = sorted(candidates, key=lambda x: (-x[-1], -x[-2], x[0]))
approved = []
for i in candidates:
    if s > 0:
        approved.append(i)
        s -= 1
ans = 0
for i in candidates:
    if i[-1] == 154:
        ans += 1
print(ans)
