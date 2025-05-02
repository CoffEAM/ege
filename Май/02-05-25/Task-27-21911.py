from math import dist

def centr(clus):
    distanse = []
    for dot1 in clus:
        sum_d = 0
        for dot2 in clus:
            sum_d += dist(dot1, dot2)
        distanse.append([sum_d, dot1])
    return min(distanse)[1]

with open('txt/27_A_21911.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centr1 = centr(clusters[0])
centr2 = centr(clusters[1])
p_x = (centr1[0] + centr2[0]) / 2
p_y = (centr1[1] + centr2[1]) / 2
print(int(p_x * 10000), int(p_y * 10000))

with open('txt/27_B_21911.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centr1 = centr(clusters[0])
centr2 = centr(clusters[1])
centr3 = centr(clusters[2])
p_x = (centr1[0] + centr2[0] + centr3[0]) / 3
p_y = (centr1[1] + centr2[1] + centr3[1]) / 3
print(int(p_x * 10000), int(p_y * 10000))
