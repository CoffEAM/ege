from math import dist

def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        distance.append([sumd, dot1])
    return min(distance)[1]

with open('txt/27A_18623.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 1.5
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

c1, c2 = centroid(clusters[0]), centroid(clusters[1])
p_x = (c1[0] + c2[0]) / 2
p_y = (c1[1] + c2[1]) / 2
print(int(p_x * 100000), int(p_y * 100000))

with open('txt/27B_18623.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 1
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

c1, c2, c3 = centroid(clusters[0]), centroid(clusters[1]), centroid(clusters[2])
p_x = (c1[0] + c2[0] + c3[0]) / 3
p_y = (c1[1] + c2[1] + c3[1]) / 3
print(int(p_x * 100000), int(p_y * 100000))
