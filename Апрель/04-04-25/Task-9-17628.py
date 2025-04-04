def f(nums):
    return max(nums) + min(nums) <= sum(nums) - (max(nums) + min(nums))

with open('txt/9_17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f(i):
        ans += 1
print(ans)
