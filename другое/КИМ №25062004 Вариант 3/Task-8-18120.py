from itertools import product

cnt = 0
for pos, val in enumerate(product(sorted('ПРЕСТОЛ'), repeat=5), start=1):
    st = ''.join(val)
    if pos % 2 == 1 and st[-1] in 'ЕО' and st.count('П') + st.count('Р') + st.count('С') + st.count('Т') + st.count(
        'Л') <= 3:
        cnt += 1
print(cnt)
