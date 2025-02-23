with open('txt/17_9840.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-2:]=='39' and 1000<=abs(i)<=9999])
pars = [[arr[i], arr[i+1]] for i in range(len(arr) - 1)]
ans = []
for para in pars:
    k = sum(1 for i in para if 1000<=abs(i)<=9999)
    if k == 1 and sum(para)**2 <= maxx**2:
        ans.append(sum(para))
print(len(ans), max(ans))
