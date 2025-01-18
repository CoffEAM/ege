arr = open('txt/26_4604.txt').readlines()
boxes = sorted([int(i) for i in arr[1:]], reverse=True)
cnt = 1
ansbox = []
maxx = max(boxes)
for i in boxes:
    if i+3<=maxx:
        maxx = i
        cnt += 1
        ansbox.append(i)

print(cnt,min(ansbox))


