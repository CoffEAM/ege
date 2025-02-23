with open('txt/17_18582.txt') as file:
    arr = [int(i) for i in file]

minn = min(arr)
ans = []
for i in range(len(arr) - 2):
    tr = arr[i:i + 3]
    u = len([1 for i in tr if i < 0]) > len([1 for i in tr if i > 0])
    if u and str(sum(tr))[-1] == str(minn)[-1]:
        ans.append(abs(sum(tr)))
print(len(ans), max(ans))
