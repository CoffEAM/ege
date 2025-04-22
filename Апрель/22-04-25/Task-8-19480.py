from itertools import permutations

ans = 0
for i in set(permutations(sorted('ПАРИЖАНКА'))):
    i = ''.join(i)
    cnt = sum(1 for x in range(len(i) - 1) if i[x:x+2] in ['АА', 'ИИ', 'АИ', 'ИА'])
    if cnt == 1:
        ans += 1
print(ans)
