from math import dist

def edges(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return max(dists)[1]

with open('txt/27.17.A_19566.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [edges(cluster) for cluster in clusters[:2]]
t_x = sum(center[0] for center in centers) / 2
t_y = sum(center[1] for center in centers) / 2
print(int(t_x * 10000), int(t_y * 10000))


with open('txt/27.17.B_19566.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1.5:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [edges(cluster) for cluster in clusters[:4]]
t_x = sum(center[0] for center in centers) / 4
t_y = sum(center[1] for center in centers) / 4
print(int(t_x * 10000), int(t_y * 10000))
