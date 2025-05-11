from math import prod

def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(2) == 4 and cnts.count(1) == 2

def f2(nums):
    u1 = max([i for i in nums if nums.count(i) > 1])**2
    u2 = prod([i for i in nums if nums.count(i) == 1])
    return u1 > u2

with open('txt/9_18134.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
