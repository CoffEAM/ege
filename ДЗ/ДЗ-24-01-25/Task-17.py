arr = open('txt/17_8562.txt').readlines()
arrr = [int(i) for i in arr]
arr = [[int(arr[i]), int(arr[i+1])] for i in range(len(arr)-1)]
minn = min(i for i in arrr if 0<i<100 and i%10==1)**2

ans = 0
summ = []
for i in arr:
    cnt = 0
    for j in i:
        if j**2<minn:
            cnt += 1
    if cnt == 1:
        if sum(i) >= 0:
            ans += 1
            summ.append(sum(i))
print(ans, min(summ))



