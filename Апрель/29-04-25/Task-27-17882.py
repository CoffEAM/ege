from math import dist
#
# def centroid(cluster):
#     distance = []
#     for dot in cluster:
#         sum_dist = 0
#         for dot2 in cluster:
#             sum_dist += dist(dot, dot2)
#         distance.append([sum_dist, dot])
#     return min(distance)[1]
#
# with open('txt/27_A_17882.txt') as file:
#     cluster1 = []
#     cluster2 = []
#     for i in file:
#         x, y = map(float, i.split())
#         if x < 1:
#             cluster1.append([x, y])
#         else:
#             cluster2.append([x, y])
#
# center1 = centroid(cluster1)
# center2 = centroid(cluster2)
#
# p_x = (center1[0] + center2[0]) / 2
# p_y = (center1[1] + center2[1]) / 2
# print(int(p_x * 10000), int(p_y * 10000))
from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('txt/27_B_17882.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 4:
            cluster1.append([x, y])
        elif 4 < y < 7:
            cluster2.append([x, y])
        else:
            cluster3.append([x, y])

centroid1 = centroid(cluster1)
centroid2 = centroid(cluster2)
centroid3 = centroid(cluster3)

p_x = (centroid1[0] + centroid2[0] + centroid3[0]) / 3
p_y = (centroid1[1] + centroid2[1] + centroid3[1]) / 3

print(int(p_x * 10000), int(p_y * 10000))
