from math import dist


def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sum_d = 0
        for dot2 in cluster:
            sum_d += dist(dot1, dot2)
        distance.append([sum_d, dot1])
    return min(distance)[1]


with open('txt/27_A_21720.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1.5
clusters = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                data.remove(dot2)
                cl.append(dot2)
    clusters.append(cl)

c1, c2 = centroid(clusters[0]), centroid(clusters[1])
p_x = (c1[0] + c2[0]) / 2
p_y = (c1[1] + c2[1]) / 2
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))

with open('txt/27_B_21720.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1.5
clusters = []
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2) < eps:
                data.remove(dot2)
                cl.append(dot2)
    clusters.append(cl)

c1, c2, c3 = centroid(clusters[0]), centroid(clusters[1]), centroid(clusters[2])
p_x = (c1[0] + c2[0] + c3[0]) / 3
p_y = (c1[1] + c2[1] + c3[1]) / 3
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))
