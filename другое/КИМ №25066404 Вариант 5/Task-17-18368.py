arr = open('txt/17_18368.txt').readlines()
arr = [int(i) for i in arr]
minn = min(i for i in arr if str(i)[-1]=='7')
troyki = [[arr[i], arr[i+1], arr[i+2]] for i in range(len(arr) - 2)]

cnt = 0
proizvedeniya = []
for troyka in troyki:
    count = 0
    proizvedenie = 1
    for chislo in troyka:
        if 100000 > abs(chislo) > 9999:
            count += 1
        proizvedenie *= chislo
    if count >= 1 and proizvedenie%minn==0:
        cnt += 1
        proizvedeniya.append(proizvedenie)
print(cnt, max(proizvedeniya))


