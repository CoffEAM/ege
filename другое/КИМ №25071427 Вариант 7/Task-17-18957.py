with open('txt/17_18957.txt') as file:
    arr = [int(i) for i in file]

maxx = max(arr)

ans = []
for i in range(len(arr)-2):
    num1, num2, num3 = arr[i:i+3]
    cnt = [1 for i in [num1, num2, num3] if '0' in str(i)]
    if sum(cnt) >= 2 and num1+num2+num3 < maxx/2:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))
