with open('txt/17_2399.txt') as file:
    data = [int(i) for i in file]

ch = [str(i) for i in data if i % 35 == 0]
suum = 0
for i in ch:
    for num in i:
        suum += int(num)
ans = []
for i in range(len(data) - 1):
    nums = data[i:i+2]
    u1 = 0
    if (nums[0] > suum >= nums[1]) and (hex(nums[1])[-2:] == 'ef') and not((nums[1] > suum >= nums[0]) and (hex(nums[0])[-2:] == 'ef')) or \
        (nums[1] > suum >= nums[0]) and (hex(nums[0])[-2:] == 'ef') and not((nums[0] > suum >= nums[1]) and (hex(nums[1])[-2:] == 'ef')):
        u1 = 1
    if u1 == 1:
        ans.append(sum(nums))
print(len(ans), min(ans))
