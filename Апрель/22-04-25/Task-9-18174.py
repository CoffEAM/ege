def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(2) == 2 and cnts.count(1) == 4

def f2(nums):
    otr = sum(i for i in nums if i < 0)
    pol = sum(i for i in nums if i > 0)
    return abs(otr) > pol

with open('txt/9_18174.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i):
        ans += 1
print(ans)
