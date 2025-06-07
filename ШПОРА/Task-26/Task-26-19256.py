with open('txt/26_19256.txt') as file:
    n = int(file.readline())
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
students = {}
for i in range(len(data) - 1):
    num1, task1 = data[i][0], data[i][1]
    num2, task2 = data[i+1][0], data[i+1][1]
    if num1 == num2 and task1 + 1 == task2:
        if num1 not in students:
            students[num1] = 1
        students[num1] += 1
print(students)
