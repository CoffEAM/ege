with open('txt/17_17680.txt') as file:
    arr = [int(i) for i in file]
minn = min(i for i in arr if i > 0 and i%41==0)
pars = [[arr[i], arr[i+1]] for i in range(len(arr)-1)]
ans = []
for para in pars:
    if len(set(para)) == len(para):
        if abs(max(para)-min(para))%minn==0:
            ans.append(sum(para))
print(len(ans), max(ans))
