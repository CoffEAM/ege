with open('txt/17_17558.txt') as file:
    arr = [int(i) for i in file]

count = sum(1 for i in arr if abs(i)%32==0)
pars = [[arr[i], arr[i+1]] for i in range(len(arr) - 1)]
ans = []
for para in pars:
    k = sum(1 for i in para if i < 0)
    if k >= 1 and sum(para) < count:
        ans.append(sum(para))
print(len(ans), max(ans))
