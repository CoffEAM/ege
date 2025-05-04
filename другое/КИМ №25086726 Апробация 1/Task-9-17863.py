def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(3) == 3 and cnts.count(1) == 3

def f2(nums):
    u1 = sum(i for i in nums if nums.count(i) > 1) ** 2
    u2 = sum(i for i in nums if nums.count(i) == 1) ** 2
    return u1 > u2

with open('txt/9_17863.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
