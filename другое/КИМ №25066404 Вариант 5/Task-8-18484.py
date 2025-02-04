from itertools import product

alph = ''.join(sorted(set('ПАВСИКАКИЙ')))
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 'АА' in val or 'ИИ' in val or 'АИ' in val or 'ИА' in val:
        cnt += 1
        if val == 'КАКААА':
            print(cnt, val)

