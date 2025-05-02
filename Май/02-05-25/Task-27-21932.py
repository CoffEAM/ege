from math import dist

def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        distance.append([sumd, dot1])
    return min(distance)[1]

with open('txt/27_A_21932.txt') as file:
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

c1, c2 = centroid(clusters[0]), centroid(clusters[1])
p_x = c2[0]
p_y = c1[1]
print(int(p_x * 10000), int(p_y * 10000))


with open('txt/27_B_21932.txt') as file:
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

c1, c2, c3 = centroid(clusters[0]), centroid(clusters[1]), centroid(clusters[2])
p_x = c3[0]
p_y = c2[1]
print(int(p_x * 10000), int(p_y * 10000))
