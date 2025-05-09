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

with open('txt/27.13.A_19567.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 1:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centers = [centroid(cl) for cl in clusters]
p_x = sum(c[0] for c in centers) / 2
p_y = sum(c[1] for c in centers) / 2
print(int(abs(p_x * 10000)), int(abs(p_y * 10000)))


with open('txt/27.13.B_19567.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 0.5:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centers = [centroid(cl) for cl in clusters]
p_x = sum(c[0] for c in centers) / 6
p_y = sum(c[1] for c in centers) / 6
print(int(abs(p_x * 10000)), int(abs(p_y * 10000)))
