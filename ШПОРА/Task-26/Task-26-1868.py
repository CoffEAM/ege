with open('txt/26_1868.txt') as file:
    n = int(file.readline())
    people = [list(map(int, i.split())) for i in file]

people = sorted(people, key=lambda x: (-x[0], x[1]))
for place1, place2 in zip(people, people[1:]):
    if place1[0] == place2[0]:
        if place2[1] - place1[1] - 1 == 2:
            print(place1[0], place1[1] + 1)
            break
