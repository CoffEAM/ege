with open('txt/17_19486.txt') as file:
    arr = [int(i) for i in file]

cnt = sum(1 for i in arr if str(i)[-1]=='7')

ans = []
for i in range(len(arr)-1):
    para = arr[i:i+2]
    u1 = sum([1 for i in para if i<0])
    u2 = sum([1 for i in para if i>0])
    if u1==u2==1 and sum(para)<cnt:
        ans.append(sum(para))
print(len(ans), max(ans))
