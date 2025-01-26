arr = open('txt/Txt-17-19249.txt').readlines()
arr = [int(i) for i in arr]
troiki = [[arr[i], arr[i + 1], arr[i + 2]] for i in range(len(arr) - 2)]

maxx = max(i for i in arr if 9999<i<100000 and str(i)[-2:]=='43')**2

cnt = 0
ans = []
for i in troiki:
    summ = 0
    pat = 0
    for j in i:
        if len(str(abs(j))) == 5 and str(j)[-2:] == '43':
            pat += 1
        summ += j**2
    if pat >= 1 and summ<=maxx:
        cnt += 1
        ans.append(summ)

print(cnt, min(ans))
