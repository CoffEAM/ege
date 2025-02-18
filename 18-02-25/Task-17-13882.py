with open('txt/17_13882.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if i%401==0])
ans = []
for i in range(len(arr)-3):
    troika = arr[i:i+3]
    u = [sum(map(int, str(i))) for i in troika]
    if len(set(u))==len(u) and sum(troika) > maxx:
        ans.append(sum(troika))
print(len(ans), min(ans))
