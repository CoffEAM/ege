arr = open('txt/09_17672.txt').readlines()
arr = [list(map(int, i.split())) for i in arr]

cnt = 0
for i in arr:
    sum1 = max(i)+min(i)
    sum2 = sum(i)-sum1
    if sum1 < sum2:
        cnt += 1
print(cnt)


