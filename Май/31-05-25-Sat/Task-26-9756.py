with open('txt/26_9756.txt') as file:
    N = int(file.readline())
    times = []
    for i in file:
        num1, num2 = map(int, i.split())
        times.append([num1, num2, num2-num1])

times = sorted(times, key=lambda x: (x[0], x[1], x[2]))
arr = [times[0]]
for time in times[1:]:
    if time[0] >= arr[-1][1]:
        arr.append(time)
print(arr)
