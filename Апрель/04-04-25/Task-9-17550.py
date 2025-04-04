def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 3 and cnt.count(1) == 3

def f2(nums):
    pov = sum([i for i in nums if nums.count(i) != 1])**2
    nepov = sum([i for i in nums if nums.count(i) == 1])**2
    return pov > nepov

with open('txt/09_17550.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
