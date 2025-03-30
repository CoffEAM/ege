with open('txt/17_12735.txt') as file:
    arr = [int(i) for i in file]

maax = max([i for i in arr if str(i)[-2:] == '09'])
ans = []
for i in range(len(arr) - 2):
    num1, num2, num3 = arr[i:i + 3]
    cnt = 0
    for i in [num1, num2, num3]:
        if i % 7 == 0:
            cnt += 1
    if cnt == 2 and num1+num2+num3 < maax:
        ans.append(num1*num2*num3)
print(len(ans), min(ans))
