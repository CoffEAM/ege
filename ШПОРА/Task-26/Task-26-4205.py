with open('txt/26_4205.txt') as file:
    n = int(file.readline())
    trees = [list(map(int, i.split())) for i in file]

trees = sorted(trees, key=lambda x: (-x[0], x[1]))
for i in range(n - 1):
    tree1, tree2 = trees[i], trees[i + 1]
    if tree1[0] == tree2[0] and tree2[1] - tree1[1] - 1 == 13:
        print(tree1[0], tree1[1] + 1)
        break
