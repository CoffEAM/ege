with open('txt/17_17873.txt') as file:
    arr = [int(i) for i in file]

minn = min(arr)
ans = []
for i in range(len(arr)-1):
    para = arr[i:i+2]
    k = sum(1 for i in para if i%16==minn)
    if k >= 1:
        ans.append(sum(para))
print(len(ans), max(ans))
