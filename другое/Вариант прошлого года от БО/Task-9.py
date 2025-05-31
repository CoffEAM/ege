def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(3) == 3 and cnts.count(1) == 4

def f2(nums):
    return nums == sorted(nums)

with open('txt/9_ok_11946.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if not(f1(i) and f2(i)):
        ans += 1
print(ans)
