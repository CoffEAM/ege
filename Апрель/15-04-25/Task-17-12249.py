with open('txt/17_12249.txt') as file:
    data = [int(i) for i in file]

maax = max([i for i in data if str(i)[-1] == '3' and len(str(abs(i))) == 5])
ans = []
for i in range(len(data) - 2):
    nums = data[i:i+3]
    cnt = sum(1 for i in nums if str(i)[-1] == '3')
    if cnt >= 1 and sum(nums) <= maax:
        ans.append(sum(nums))
print(len(ans), max(ans))
