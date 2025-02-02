file = open('txt/26_14625.txt').readlines()
K, R, M = map(int, file[1].split())
M = M * 2**20
files = []
for i in file[2:]:
    t, s, e = i.split()
    p = 1
    if e == 'mb':
        p = 2 ** 20
    elif e == 'kb':
        p = 2 ** 10
    s = int(s) * p
    files.append([int(t), s])

files = sorted(files, key=lambda x: -x[1])
deleted = [0] * (K+1)
last_file = 0
volume = 0

for file in files:
    if deleted[file[0]] < R and volume + file[1] < M:
        deleted[file[0]] += 1
        volume += file[1]

for file in files[::-1]:
    if deleted[file[0]] < R and volume + file[1] > M:
        deleted[file[0]] += 1
        last_file = file[1]
        break

print(sum(deleted), last_file)





