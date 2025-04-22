with open('txt/17_9840.txt') as file:
    data = [int(i) for i in file]

maax = max([i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '39'])
ans = []
for i in range(len(data) - 1):
    nums = data[i:i+2]
    u1 = sum(1 for k in nums if len(str(abs(k))) == 4) == 1
    if u1 and sum(nums) ** 2 <= maax ** 2:
        ans.append(sum(nums))
print(len(ans), max(ans))
