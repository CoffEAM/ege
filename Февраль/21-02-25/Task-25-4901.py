from fnmatch import fnmatch

# for i in range(16606, 10000000):
#     if i%6==0 and i%7==0 and i%8==0:
#         if fnmatch(str(i), '?6*6*?6'):
#             print(i)

arr = [56616, 66696, 161616, 166656, 266616, 360696, 366576]
ans = []
for i in arr:
    sum_d = sum(k for k in range(1, i // 2 + 1) if i % k == 0)
    ans.append([i, sum_d + i])

for i in ans:
    print(*i)
