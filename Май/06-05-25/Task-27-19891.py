def dist(dot1, dot2):
    return max(abs(dot1[0] - dot2[0]), abs(dot1[1] - dot2[1]))


def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        distance.append([sumd, dot1])
    return min(distance)[1]


with open('txt/27.3.A_19891.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 1
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

c1, c2 = centroid(clusters[0]), centroid(clusters[1])
p_x = (c1[0] + c2[0]) / 2
p_y = (c1[1] + c2[1]) / 2
print(int(p_x * 10000), int(p_y * 10000))


with open('txt/27.3.B_19891.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 0.5
while data:
    cluster = [data.pop()]
    for dot1 in cluster:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(c[0] for c in centers) / 2
p_y = sum(c[1] for c in centers) / 2
print(int(p_x * 10000), int(p_y * 10000))
