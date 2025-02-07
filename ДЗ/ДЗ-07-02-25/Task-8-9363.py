from itertools import permutations

cnt = 0
errors = [''.join(i) for i in permutations('ОУАЮЕ')]


for val in permutations('ХОЧУНАБЮДЖЕТ'):
    val = ''.join(val)
    for error in errors:
        if error not in val:
            cnt += 1
print(cnt)

