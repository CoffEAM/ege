from math import dist

def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot1, dot2)
        distance.append([sum_dist, dot1])
    return min(distance)[1]

with open('txt/27_A_17916.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file.readlines()[1:]:
        x, y = map(float, i.replace(',', '.').split())
        if y > 8:
            cluster1.append([x, y])
        else:
            cluster2.append([x, y])

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)

p_x = (centroid1[0] + centroid2[0]) / 2
p_y = (centroid1[1] + centroid2[1]) / 2
print(int(p_x * 10000), int(p_y * 10000))

with open('txt/27_B_17916.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    for i in file.readlines()[1:]:
        x, y = map(float, i.replace(',', '.').split())
        if y > 14:
            cluster1.append([x, y])
        elif 10 < y < 14:
            cluster2.append([x, y])
        elif 6 < y < 8:
            cluster3.append([x, y])
        elif y < 6 and x < 8:
            cluster4.append([x, y])
        else:
            cluster5.append([x, y])

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)
centroid3 = centroid(cluster3)
centroid4 = centroid(cluster4)
centroid5 = centroid(cluster5)

p_x = (centroid1[0] + centroid2[0] + centroid3[0] + centroid4[0] + centroid5[0]) / 5
p_y = (centroid1[1] + centroid2[1] + centroid3[1] + centroid4[1] + centroid5[1]) / 5
print(int(p_x * 10000), int(p_y * 10000))
