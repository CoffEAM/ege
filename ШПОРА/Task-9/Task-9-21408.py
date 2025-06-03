def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(3) == 6 and cnts.count(1) == 1

def f2(nums):
    num1 = max([i for i in nums if nums.count(i) > 1])
    num2 = min([i for i in nums if nums.count(i) == 1])
    return num1 > num2

with open('txt/9_21408.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
