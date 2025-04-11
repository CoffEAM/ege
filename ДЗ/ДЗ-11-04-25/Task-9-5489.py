def f1(nums):
    return len(nums) == len(set(nums))


def f2(nums):
    chet = sum(1 for i in nums if i % 2 == 0)
    nech = sum(1 for i in nums if i % 2 == 1)
    return chet > nech


def f3(nums):
    chet = sum(i for i in nums if i % 2 == 0)
    nech = sum(i for i in nums if i % 2 == 1)
    return chet < nech


with open('txt/9_5489.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        ans += 1
print(ans)
