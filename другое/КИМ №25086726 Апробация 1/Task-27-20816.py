from math import dist

def centroid(cluster):
    d = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        d.append([sumd, dot1])
    return min(d)[1]

with open('txt/27_A_20816.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 2
while data:
    clust = [data.pop()]
    for d1 in clust:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                data.remove(d2)
                clust.append(d2)
    clusters.append(clust)

c1, c2 = centroid(clusters[0]), centroid(clusters[1])
p_x = (c1[0] + c2[0]) / 2
p_y = (c1[1] + c2[1]) / 2
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))

with open('txt/27_B_20816.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 1.5
while data:
    clust = [data.pop()]
    for d1 in clust:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                data.remove(d2)
                clust.append(d2)
    clusters.append(clust)

c1, c2, c3 = centroid(clusters[0]), centroid(clusters[1]), centroid(clusters[2])
p_x = (c1[0] + c2[0] + c3[0]) / 3
p_y = (c1[1] + c2[1] + c3[1]) / 3
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))
