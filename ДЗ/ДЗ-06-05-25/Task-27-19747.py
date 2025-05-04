from math import dist


def centroid(cluster):
    distance = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        distance.append([sumd, dot1])
    return min(distance)[1]


with open('txt/27A_19747.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if y < 5:
            cluster1.append([x, y])
        elif x < 5:
            cluster2.append([x, y])
        else:
            cluster3.append([x, y])

c1, c2, c3 = centroid(cluster1), centroid(cluster2), centroid(cluster3)
p_x = (c1[0] + c2[0] + c3[0]) / 3
p_y = (c1[1] + c2[1] + c3[1]) / 3
print(abs(int(p_x * 100000)), abs(int(p_y * 100000)))

with open('txt/27B_19747.txt') as file:
    g1 = []
    g2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if x < 10 and y < 10:
            g1.append([x, y])
        elif y > 10 and x > 10:
            g2.append([x, y])
        else:
            cluster3.append([x, y])

cluster1 = []
cluster2 = []
for x, y in g1:
    if y > x:
        cluster1.append([x, y])
    elif y < x:
        cluster2.append([x, y])
cluster4 = []
cluster5 = []
for x, y in g2:
    if y > x:
        cluster5.append([x, y])
    elif y < x:
        cluster4.append([x, y])

c1,c2,c3,c4,c5 = centroid(cluster1), centroid(cluster2), centroid(cluster3), centroid(cluster4), centroid(cluster5)
p_x = (c1[0] + c2[0] + c3[0] + c4[0] + c5[0]) / 5
p_y = (c1[1] + c2[1] + c3[1] + c4[1] + c5[1]) / 5
print(abs(int(p_x * 100000)), abs(int(p_y * 100000)))
