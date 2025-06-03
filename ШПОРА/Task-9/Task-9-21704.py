def f1(nums):
    return sorted(nums, reverse=True) == nums

def f2(nums):
    ar1 = (min(nums) + max(nums))/2
    ar2 = (sum(nums) - ar1*2)/5
    return ar1 > ar2

with open('txt/9_21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for i in data:
    if f1(i) and f2(i):
        print(sum(i))
        break
