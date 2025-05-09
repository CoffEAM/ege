from math import dist

def centroid(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return min(dists)[1]

with open('txt/27A_18629.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [centroid(c) for c in clusters[:2]]
p_x = sum(c[0] for c in centers) / 2
p_y = sum(c[1] for c in centers) / 2
print(int(p_x * 100000), int(p_y * 100000))

with open('txt/27B_18629.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [centroid(c) for c in clusters[:3]]
p_x = sum(c[0] for c in centers) / 3
p_y = sum(c[1] for c in centers) / 3
print(int(p_x * 100000), int(p_y * 100000))
