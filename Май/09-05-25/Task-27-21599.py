from math import dist

def centroid(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return min(dists)[1]

with open('txt/27_A_21599.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if y > 2*x - 18:
            cluster1.append([x, y])
        elif y > -6:
            cluster2.append([x, y])
        else:
            cluster3.append([x, y])

centers = [centroid(cluster) for cluster in [cluster1, cluster2, cluster3]]
p_x = sum(c[0] for c in centers) / 3
p_y = sum(c[1] for c in centers) / 3
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))

with open('txt/27_B_21599.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    cluster6 = []
    for i in file:
        x, y = map(float, i.replace(',', '.').split())
        if y < -1.5 * x - 18.5:
            cluster1.append([x, y])
        elif x < -10:
            cluster2.append([x, y])
        elif y > 2 * x + 12:
            cluster3.append([x, y])
        elif y > x + 2:
            cluster4.append([x, y])
        elif y > -5:
            cluster5.append([x, y])
        else:
            cluster6.append([x, y])

centers = [centroid(c) for c in [cluster1, cluster2, cluster3, cluster4, cluster5, cluster6]]
p_x = sum(c[0] for c in centers) / 6
p_y = sum(c[1] for c in centers) / 6
print(abs(int(p_x * 10000)), abs(int(p_y * 10000)))
