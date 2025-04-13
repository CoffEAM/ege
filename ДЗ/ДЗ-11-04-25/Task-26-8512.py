with open('txt/26_8512.txt') as file:
    K = int(file.readline())
    N = 987
    data = [list(map(int, i.split())) for i in file.readlines()[1:]]

places = [0] * (K + 1)
data = sorted(data)

for i in data:
    for place in range(len(places)):
        if places[place] == 0:
            places[place] = 1
            break
