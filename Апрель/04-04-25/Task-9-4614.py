with open('txt/9_4614.txt') as file:
    data = [list(map(int, i.split())) for i in file]

def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    return len(set(nums)) == 3

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
