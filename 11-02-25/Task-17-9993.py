def prost(num):
    if num < 2:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1


with open('txt/17_9993.txt') as file:
    arr = [int(i) for i in file]
maxx = max(i for i in arr if str(i)[-2:] == '17')
pars = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]

ans = []
for para in pars:
    k = prost(abs(para[0])) + prost(abs(para[1]))
    if k == 1 and abs(sum(para)) % maxx == 0:
        ans.append(para[0] * para[1])
print(len(ans), max(ans))
