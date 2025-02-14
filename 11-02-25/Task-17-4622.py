with open('txt/17_4622.txt') as file:
    arr = [int(i) for i in file]

minn = min([i for i in arr if i > 0 and i%19==0])
pars = [[arr[i], arr[i+1]] for i in range(len(arr)-1)]
cnt = 0
summs = []
for para in pars:
    if sum(para) < minn:
        cnt += 1
        summs.append(max(para)+min(para))

print(cnt, max(summs))

