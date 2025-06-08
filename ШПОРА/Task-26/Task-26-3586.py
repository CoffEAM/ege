with open('txt/26_3586.txt') as file:
    n = int(file.readline())
    trees = [list(map(int, i.split())) for i in file]

trees = sorted(trees, key=lambda x: (-x[0], x[1]))
rows = []
for tree1, tree2 in zip(trees, trees[1:]):
    if tree1[0] == tree2[0]:
        rows.append([tree2[1] - tree1[1] - 1, tree1[0]])
print(max(rows))
