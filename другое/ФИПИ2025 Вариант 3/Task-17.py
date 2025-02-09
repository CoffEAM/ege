arr = open('txt/17var03.txt').readlines()
arr = [int(i) for i in arr]
minn = min(arr)
pars = [[arr[i], arr[i+1]] for i in range(len(arr)-1)]

cnt = 0
raznosti = []
for para in pars:
    summ = para[0]%44 + para[1]%44
    if summ==minn:
        cnt += 1
        raznosti.append(abs(para[0]-para[1]))
print(cnt, min(raznosti))
# 178 593

