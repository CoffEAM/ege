def f1(nums):
    counts = [nums.count(i) for i in nums]
    return counts.count(2) == 2 and counts.count(1) == 4

def f2(nums):
    arr = [i for i in nums if nums.count(i) == 1]
    sr_ar = sum(arr) / len(arr)
    return (sum(nums) - sum(arr))/2 >= sr_ar

with open('txt/09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, nums in enumerate(data, start=1):
    if f1(nums) and f2(nums):
        print(pos)
        break
