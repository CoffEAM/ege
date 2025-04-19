with open('txt/26_2651.txt') as file:
    N = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
marks = []
for year in range(31):
    m = []
    for mark in range(1, 9):
        m.append(data.count([year + 1961, mark]))
    marks.append(m)
ans1 = 0
for i in marks:
    ans1 += i.count(0)
print(ans1)
ans2 = 0
for i in marks[::-1]:
    if i.count(0) == 4:
        ans2 = marks.index(i) + 1961
        break
print(ans2)
