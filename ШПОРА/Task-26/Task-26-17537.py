with open('txt/26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data, reverse=True)
suitable = [m] * (k + 1)
for i in data:
    suitable[i[1]] = min(suitable[i[1]], i[0] - 1)
ans = []
for i in range(2, k + 1):
    place1, place2 = suitable[i - 1], suitable[i]
    ans.append([min(place1, place2), i])
print(max(ans))
