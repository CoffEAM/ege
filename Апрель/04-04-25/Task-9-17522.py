def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 2

with open('txt/9_17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i)and f2(i):
        ans += 1
print(ans)
