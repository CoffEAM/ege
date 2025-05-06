from math import dist


def centroid(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return min(dists)[1]


with open('txt/27.21.A_19715.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 2:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [centroid(cluster) for cluster in clusters[:2]]
p_x = sum(center[0] for center in centers) / 2
p_y = sum(center[1] for center in centers) / 2
print(int(p_x * 10000), int(p_y * 10000))


with open('txt/27.21.B_19715.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 3:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [centroid(cluster) for cluster in clusters[:4]]
p_x = sum(center[0] for center in centers) / 4
p_y = sum(center[1] for center in centers) / 4
print(int(p_x * 10000), int(p_y * 10000))
