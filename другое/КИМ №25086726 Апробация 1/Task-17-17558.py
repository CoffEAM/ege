with open('txt/17_17558.txt') as file:
    data = [int(i) for i in file]

u = sum(1 for i in data if i % 32 == 0)
ans = []
for i in range(len(data) - 1):
    nums = data[i:i+2]
    u1 = sum(1 for k in nums if k < 0)
    if sum(nums) < u and u1 >= 1:
        ans.append(sum(nums))
print(len(ans), max(ans))
