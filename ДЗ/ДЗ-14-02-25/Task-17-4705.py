with open('txt/17_4705.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-1]=='3'])
ans = []
for i in range(len(arr)-1):
    para = arr[i:i+2]
    k = sum(1 for i in para if str(i)[-1]=='3')
    if k == 1 and para[0]**2+para[1]**2 >= maxx**2:
        ans.append(para[0]**2+para[1]**2)
print(len(ans), max(ans))
