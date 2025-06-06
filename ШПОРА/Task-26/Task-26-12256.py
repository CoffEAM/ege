with open('txt/26_12256.txt') as file:
    s, n = map(int, file.readline().split())
    data = [int(i) for i in file]

data = sorted(data)
ans = []
for i in data:
    if s - i >= 0:
        ans.append(i)
        s -= i
s = s + ans[-1]
ans.remove(ans[-1])
for i in data[::-1]:
    if s - i >= 0:
        ans.append(i)
        break
print(len(ans), ans[-1])
