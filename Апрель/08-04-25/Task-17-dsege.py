with open('17.txt') as file:
    data = [int(i) for i in file]

suum = sum([i for i in data if i < 0])
ans = 0
max_sum = 0
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    pr = max(num1, num2, num3) * min(num1, num2, num3)
    if pr > suum:
        ans += 1
    if num1 + num2 + num3 > max_sum:
        max_sum = num1 + num2 + num3
print(ans, abs(max_sum))
