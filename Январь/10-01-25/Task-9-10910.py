def f1(line):
    return line.count(min(line)) == 1

def f2(line):
    return len(set(line)) != len(line)

def f3(line):
    pov = [i for i in line if line.count(i)>1]
    return min(line)+max(line) < sum(pov)

with open('Txt-9-10910.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

cnt = 0
for i in arr:
    if all([f1(i), f2(i), f3(i)]):
        cnt += 1
print(cnt)



