from math import dist
import turtle as t

def centroid(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return min(dists)[1]

with open('txt/2707_A.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 0.2:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / 2
p_y = sum(center[1] for center in centers) / 2
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))


with open('txt/2707_B.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 0.2:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / 3
p_y = sum(center[1] for center in centers) / 3
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))
