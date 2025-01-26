from itertools import product, repeat

sogl = 'МНС'
gl = 'ИУ'

ans = []
for pos, val in enumerate(product(sorted('МИНУС'), repeat=4), start=1):
    val = ''.join(val)
    sogls = sum(1 for i in val if i in sogl)
    gls = sum(1 for i in val if i in gl)
    if sogls >= gls:
        ans.append(pos)
print(ans[-1])


