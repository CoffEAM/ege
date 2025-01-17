sts = open('imaev/24_stat21apr.txt').readlines()

arr = [i for i in sts if i.count('G')<25]
ans = []
for i in arr:
    for j in i:
        maxx = i.rfind(j)-i.find(j)
        ans.append(maxx)
print(max(ans))


