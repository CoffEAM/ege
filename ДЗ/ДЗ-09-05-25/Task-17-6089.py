with open('txt/17_6089.txt') as file:
    data = [int(i) for i in file]

maximum = max([i for i in data if str(i)[-1] == '2'])
ans = []
for num in data:
    if num % 3 == 0 and num % 7 != 0 and num % 17 != 0:
        if maximum % num == 0:
            ans.append(num)
print(len(ans), max(ans))
