def f1(nums):
    return [nums.count(i) for i in nums].count(1) < len(nums)

def f2(nums):
    cnt = sum(1 for i in nums if i % 2 == 1)
    return cnt == 3

with open('txt/9_6262.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if (f1(i) and not(f2(i))) or (not(f1(i)) and f2(i)):
        ans += 1
print(ans)
