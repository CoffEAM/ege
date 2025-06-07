with open('txt/26_21719.txt') as file:
    n = int(file.readline())
    students = {}
    data = sorted([list(map(int, i.split())) for i in file])
    for i in range(n - 1):
        num1, task1 = data[i][0], data[i][1]
        num2, task2 = data[i+1][0], data[i+1][1]
        if num1 == num2 and task2 - task1 == 2:
            if num1 not in students:
                students[num1] = 0
            students[num1] += 1
print(max(students.values()))
for i in students:
    if students[i] == 82:
        print(i)
        break
