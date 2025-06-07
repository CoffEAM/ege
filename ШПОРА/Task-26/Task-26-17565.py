with open('txt/26_17565.txt') as file:
    n, s = map(int, file.readline().split())
    candidates = []
    for i in file:
        arr = list(map(int, i.split()))
        arr.append(sum(arr[1:]))
        candidates.append(arr)

candidates = sorted(candidates, key=lambda x: (-x[-1], -x[-2], x[0]))
print(candidates)
approved = []
for candidate in candidates:
    if s > 0:
        approved.append(candidate)
        s -= 1
ans = 0
for candidate in candidates:
    if candidate[-1] == 159:
        ans += 1
print(approved[-1], ans)
