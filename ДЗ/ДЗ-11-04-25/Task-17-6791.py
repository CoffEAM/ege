with open('txt/17_6791.txt') as file:
    data = [int(i) for i in file]

miin = min([i for i in data if str(i)[-2:] == '68'])**2
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    cnt = sum(1 for i in [num1, num2] if str(i)[-2:] == '68')
    if cnt == 1 and num1**2 + num2**2 >= miin:
        ans.append(num1**2+num2**2)
print(len(ans), max(ans))
