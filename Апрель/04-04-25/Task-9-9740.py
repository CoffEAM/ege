def f1(nums):
    arr = [nums.count(i) for i in nums]
    return arr.count(3) == 3 and arr.count(1) == 4

def f2(nums):
    arr = [i for i in nums if nums.count(i) == 1]
    sr_ar = sum(arr) / len(arr)
    return sr_ar <= (sum(nums) - sum(arr))/3

with open('txt/9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
