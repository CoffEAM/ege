from math import dist

def anticentroid(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return max(dists)[1]

with open('txt/27_A_21931.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 2:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

anticenters = [anticentroid(c) for c in clusters]
p_x = anticenters[1][0]
p_y = anticenters[0][1]
print(int(p_x * 10000), int(p_y * 10000))

with open('txt/27_B_21931.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1.5:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

anticenters = [anticentroid(c) for c in clusters]
p_x = anticenters[2][0]
p_y = anticenters[1][1]
print(int(p_x * 10000), int(p_y * 10000))
