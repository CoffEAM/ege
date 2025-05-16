from math import dist

def gorod(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return min(dists)[1]

with open('txt/27_A_18884.txt') as file:
    data = [list(map(int, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 2:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [gorod(c) for c in clusters]
s_x = sum([c[0] for c in centers]) / 2
s_y = sum([c[1] for c in centers]) / 2
print(int(abs(s_x)), int(abs(s_y)))

with open('txt/27_B_18884.txt') as file:
    data = [list(map(int, i.split())) for i in file]

clusters = []
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= 3:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

centers = [gorod(c) for c in clusters]
s_x = sum([c[0] for c in centers]) / 3
s_y = sum([c[1] for c in centers]) / 3
print(int(abs(s_x)), int(abs(s_y)))

