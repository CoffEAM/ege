arr = open('txt/17_4597.txt').readlines()
arr = [int(i) for i in arr]
minn = min(arr)
pari = [[arr[i], arr[i+1]] for i in range(len(arr)-1)]
cnt = 0
summs = []
for para in pari:
    k = 0
    for num in para:
        if num%117==minn:
            k += 1
    if k >= 1:
        cnt += 1
        summs.append(sum(para))
print(cnt, max(summs))


