with open('txt/17_19249.txt') as file:
    arr = [int(i) for i in file]

maxx = max([i for i in arr if str(i)[-2:]=='43' and len(str(abs(i)))==5])
ans = []
for i in range(len(arr) - 2):
    num1, num2, num3 = arr[i:i+3]
    k = sum(1 for l in [num1,num2,num3] if str(l)[-2:]=='43' and 10000<=abs(l)<=99999)
    if k >= 1 and num1**2+num2**2+num3**2 <= maxx**2:
        ans.append(num1**2+num2**2+num3**2)
print(len(ans), min(ans))
