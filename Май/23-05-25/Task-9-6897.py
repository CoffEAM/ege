def f1(nums):
    return max(nums) < (sum(nums) - max(nums))

def f2(nums):
    u1 = max(nums) + min(nums)
    u2 = sum(nums) - u1
    return u1 != u2

with open('txt/9_6897.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
