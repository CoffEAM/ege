with open('txt/17_17530.txt') as file:
    arr = [int(i) for i in file]

minn = min(arr)
pars = [[arr[i], arr[i+1]] for i in range(len(arr)-1)]
ans = []
for para in pars:
    k = sum(1 for i in para if i%55==minn)
    if k >= 1:
        ans.append(sum(para))
print(len(ans), min(ans))
