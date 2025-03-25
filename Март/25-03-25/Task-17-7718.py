with open('txt/17 (2)_7718.txt') as file:
    arr = [int(i) for i in file]

ans = []
for i in range(len(arr) - 1):
    num1, num2 = arr[i:i+2]
    u1 = 0
    u2 = 0
    if (num1 + num2)%18 == 0:
        u1 += 1
    if (num1*num2)%18 == 0:
        u2 += 1
    if u1 + u2 == 1 and num1 != num2:
        ans.append(num1+num2)
print(len(ans), max(ans))
