with open('txt/17_2399.txt') as file:
    data = [int(i) for i in file]

suum = sum(map(int, ''.join([str(i) for i in data if i % 35 == 0])))
ans = []
for i in range(len(data) - 1):
    nums = data[i:i+2]
    u1 = sum(1 for k in nums if k > suum)
    u2 = sum(1 for k in nums if hex(k)[-2:] == 'ef')
    if u1 == 1 and u2 == 1:
        ans.append(sum(nums))
print(len(ans), min(ans))
