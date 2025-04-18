from http.cookiejar import unmatched


def f1(nums):
    cnts = [nums.count(i) for i in nums]
    return cnts.count(2) == 4 and cnts.count(1) == 2

def f2(nums):
    return nums.count(max(nums)) == 1

def f3(nums):
    return max(nums) * min(nums) > sum(nums) - max(nums) - min(nums)

with open('txt/9_12918.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for i in data:
    if f1(i) and f2(i) and f3(i):
        print(sum(i))
        break
