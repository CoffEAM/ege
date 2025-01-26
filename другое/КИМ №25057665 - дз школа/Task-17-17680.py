arr = open('txt/17_17680.txt').readlines()
arr = [int(i) for i in arr]
minn = min(i for i in arr if i%41==0 and i>0)
arr = [[arr[i], arr[i+1]] for i in range(len(arr) - 1)]

cnt = 0
summ = []
for i in arr:
    if i[0]!=i[1]:
        raznost = max(i)-min(i)
        if raznost%minn == 0:
            cnt += 1
            summ.append(sum(i))
print(cnt, max(summ))


