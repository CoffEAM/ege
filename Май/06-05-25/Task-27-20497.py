from math import dist

def edges(cluster):
    dists = []
    for dot1 in cluster:
        sumd = 0
        for dot2 in cluster:
            sumd += dist(dot1, dot2)
        dists.append([sumd, dot1])
    return max(dists)[1]

with open('txt/27.19.A_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 0.4
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                data.remove(dot2)
                cl.append(dot2)
    clusters.append(cl)

centers = [edges(cl) for cl in clusters[:3]]
t_x = sum(center[0] for center in centers) / 3
t_y = sum(center[1] for center in centers) / 3
print(int(t_x * 10000), int(t_y * 10000))


with open('txt/27.19.B_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 2
while data:
    cl = [data.pop()]
    for dot1 in cl:
        for dot2 in data.copy():
            if dist(dot1, dot2) <= eps:
                data.remove(dot2)
                cl.append(dot2)
    clusters.append(cl)

centers = [edges(cl) for cl in clusters[:5]]
t_x = sum(center[0] for center in centers) / 5
t_y = sum(center[1] for center in centers) / 5
print(int(t_x * 10000), int(t_y * 10000))
