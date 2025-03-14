with open('txt/17_14952.txt') as file:
    data = [int(i) for i in file]

maxx = max([i for i in data if str(i)[-3:] == '121'])

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    cnt = sum([1 for i in [num1,num2,num3] if len(str(abs(i)))==4 and i%2==0])
    if cnt <= 1 and num1+num2+num3 <= maxx:
        ans.append(num1+num2+num3)
print(len(ans), max(ans))
