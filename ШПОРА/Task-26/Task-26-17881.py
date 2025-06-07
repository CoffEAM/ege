with open('txt/26_17881.txt') as file:
    n = int(file.readline())
    students = []
    for i in file:
        inf = list(map(int, i.split()))
        inf.append(sum(inf[1:])/4)
        inf.append(inf[1:].count(2))
        students.append(inf)

students = sorted(students, key=lambda x: (-x[-2], x[0], [-1]))
selected = []
for i in students:
    if len(selected) < len(students) * 0.25:
        if 2 not in i[1:-2]:
            selected.append(i)
print(selected[-1])
for i in students:
    if i[-1] > 2:
        print(i)
        break
