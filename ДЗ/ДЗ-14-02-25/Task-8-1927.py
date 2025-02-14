from itertools import product
cnt = 0
gl = 'ЯОИЕ'
for val in product('ЯСНОВИДЕЦ', repeat=5):
    val = ''.join(val)
    if  val[0] not in gl and val[-1] in gl:
        if val.count(val[0]) + val.count(val[-1]) == 2:
            cnt += 1
print(cnt)
